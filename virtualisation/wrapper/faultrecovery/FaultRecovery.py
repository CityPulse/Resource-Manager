# -*- coding: utf-8 -*-
"""
CityPulse fault recovery component

Created on Thu Jul 30 08:49:16 2015

@author: lucian.sasu@siemens.com dan.puiu@siemens.com
"""

import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class FaultRecovery:
    
    # default constructor
    def __init__(self):        
        # configuration params of the component
        self.SAMPLE_SIZE = 20
        self.NUMBER_OF_NEIGHBORS = 5
        self.SIMILARITY_PERCENTAGE = 0.30      
        
        # the reference dataset params
        self.referenceDatasetX = np.empty([0, self.SAMPLE_SIZE - 1])
        self.referenceDatasetY = np.empty([1, 0])             
        self.referenceDatasetNumberOfRows = 0
        
        # sample is a buffer vector where are kept the last SAMPLE_SIZE reported measurements
        self.sample = np.empty(self.SAMPLE_SIZE) * np.NaN
                
        # the prediction model        
        self.model = KNeighborsRegressor(n_neighbors=self.NUMBER_OF_NEIGHBORS, weights='distance', p=2, metric='minkowski')
        
        # value keeping the previous reported measurement        
        self.previousMeasurement = None
        self.n_cor = 0
      
    def addValidMeasurement(self, measurement):
        """
        method used for reporting a new valid measurement
        
        Parameters
        ----------
        measurement: an integer of double value representing the latest measurement
        
        """
        
        # valid only for the first time when there is no previous measurement
        if self.previousMeasurement is None:
            self.previousMeasurement = measurement
                        
        # the model keeps track of the measurements variation (differences from one measurement to the other) not the actual values
        valueToAdd = measurement - self.previousMeasurement

        # add the new value in the sample
        for k in range(self.SAMPLE_SIZE - 1):
            self.sample[k] = self.sample[k + 1]
        
        self.sample[self.SAMPLE_SIZE - 1] = valueToAdd
        
        
        # check if the current sample is potentialy valid to be added to the reference dataset  (sample does not contain missing values)       
        if (sum(np.isnan(self.sample)) == 0):

            # if the reference dataset is almost empty the sample will be automatically added
            if (self.referenceDatasetNumberOfRows < self.NUMBER_OF_NEIGHBORS):            
                self.referenceDatasetNumberOfRows = self.referenceDatasetNumberOfRows + 1
                self.referenceDatasetX = np.vstack((self.referenceDatasetX, self.sample[0:-1]))    
                self.referenceDatasetY = np.append(self.referenceDatasetY, self.sample[-1])
                
                if(self.referenceDatasetNumberOfRows == self.NUMBER_OF_NEIGHBORS):
                    x_train = self.referenceDatasetX
                    y_train = self.referenceDatasetY
                    self.model.fit(x_train, y_train)
            else:
                # count how many entries from the reference data set are similar to the current one
                # get the indexes of the closses entries                
                neighbours = self.model.kneighbors(self.sample[0:-1])
               
                # get the entries from the dataset for the above mentionex indexes
                neighbour_values = self.referenceDatasetX[neighbours[1], :]
                
                # compute the correlation between current sample and each entry. Count how many entries have the correlation bellow SIMILARITY_PERCENTAGE
                self.n_cor = 0
                for i in range (self.NUMBER_OF_NEIGHBORS):
                    current_corr = np.corrcoef(self.sample[0:-1], neighbour_values[0][i, :])[0, 1]
                    if (current_corr > self.SIMILARITY_PERCENTAGE):
                        self.n_cor = self.n_cor + 1
                
                # if count is bellow 2 the sample is added to the reference dataset and the model is retrained 
                if(self.n_cor < 2):
                    self.referenceDatasetNumberOfRows = self.referenceDatasetNumberOfRows + 1
                    self.referenceDatasetX = np.vstack((self.referenceDatasetX, self.sample[0:-1]))    
                    self.referenceDatasetY = np.append(self.referenceDatasetY, self.sample[-1])
                    
#                     x_train = self.referenceDatasetX
#                     y_train = self.referenceDatasetY
#                     self.model.fit(x_train,y_train )
    
    def reportInvalidMeasurement(self):
        """
        method used for reporting an invalid measurement
        
        """

        # it adds an estimation to the sample of each and every invalid report if it is posible (the prediction model works) otherwhise np.nan         
        
        pred = self.getEstimation()
        
        for k in range(self.SAMPLE_SIZE - 1):
            self.sample[k] = self.sample[k + 1]
        
        if (pred is None):
            self.sample[self.SAMPLE_SIZE - 1] = np.nan
        else:
            self.sample[self.SAMPLE_SIZE - 1] = pred  
    
    
    def getEstimation(self):
        """
        method used for optaining the estimations
        
        Returns a double value representing the estimation
        """
        if (self.referenceDatasetNumberOfRows >= self.NUMBER_OF_NEIGHBORS) & (sum(np.isnan(self.sample)) == 0):
            if(self.n_cor < 2):
                self.model.fit(self.referenceDatasetX, self.referenceDatasetY)
                
            pred = self.model.predict(self.sample[0:-1]) + self.previousMeasurement
            return pred[0]
        return None
    
    def isReady(self):
        """
        checks if the reference data set contains enough entries intorde to generate a prediction
        
        Returns a boolean value
        
        """
        return (self.referenceDatasetNumberOfRows >= self.NUMBER_OF_NEIGHBORS)
        
    def loadTrainingSet(self, reference_X, reference_Y):
        """
        this method can be used to load reference data set if needed.
        """

        self.referenceDatasetX = reference_X
        self.referenceDatasetY = reference_Y 
        self.referenceDatasetNumberOfRows = len(self.referenceDatasetY)
        
        x_train = self.referenceDatasetX
        y_train = self.referenceDatasetY
        self.model.fit(x_train, y_train) 

