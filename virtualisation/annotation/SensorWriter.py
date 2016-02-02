__author__ = 'sefki'
import saopy

import uuid
import numpy as np
import time
from thread import start_new_thread

class SensorWriter:

    def __init__(self, graphName):
        self.graphName = graphName
        pass


    def getSAOAReperesentation(self, collection):
        saoOut = saopy.SaoInfo()
        for data in collection:
            interval = saopy.tl.Interval(self.graphName+"timeinterval")
            sensor = saopy.ssn.Sensor(data.sensorID)
            foi = saopy.ssn.FeatureOfInterest("http://ict-citypulse.eu/FoI-" + str(uuid.uuid4()))
            if data.Latitude != "" and data.Longitude!="":
                location = saopy.geo.SpatialThing("http://ict-citypulse.eu/Location-" + data.sensorID)
                location.lat=str(data.Latitude)
                location.long=str(data.Longitude)
                foi.hasLocation = location
                saoOut.add(location)

            data.propertyID = data.GRAPH_BASE_URI + "PropertyID-" + str(uuid.uuid4())

            #property = saopy.prov.Entity(data.propertyID)
            sensorproperty = saopy.ssn.Property(data.propertyID)
            sensorproperty.description = data.propertyName
            sensorproperty.isPropertyOf = foi
            sensor.observes.add(sensorproperty)
            aggmtx = np.array(data.AggregationValue)
            nrows = np.atleast_2d(aggmtx).shape[1]
            ncols=np.atleast_2d(aggmtx).shape[0]
            aggregationId = self.graphName +"Aggregation-" + str(uuid.uuid4())
            aggregation = saopy.sao.StreamAnalysis(aggregationId)


            if data.AggregationMethodName == "dft":
                aggregation = saopy.sao.DiscreteFourierTransform(aggregationId)

            if data.AggregationMethodName == "dwt":
                aggregation = saopy.sao.DiscreteWaveletTransform(aggregationId)

            if data.AggregationMethodName == "sax":
                aggregation = saopy.sao.SymbolicAggregateApproximation(aggregationId)

            if data.AggregationMethodName == "paa":
                aggregation = saopy.sao.PiecewiseAggregateApproximation(aggregationId)

            if data.AggregationMethodName == "sensorsax":
                aggregation = saopy.sao.SensorSax(aggregationId)


            aggregation.value = ' '.join(map(str,aggmtx))
            aggregation.nRows = nrows
            aggregation.nColumns = ncols
            aggregation.wasAttributedTo=sensorproperty
            saoOut.add(aggregation)
            saoOut.add(sensorproperty)
            saoOut.add(sensor)
            saoOut.add(foi)

            interval.beginsAtDateTime = str(data.BeginsAtDateTime)
            interval.endsAtDateTime = str(data.EndsAtDateTime)

            aggregation.time = interval
            if data.measurementUnit!=None:
                mu = saopy.muo.UnitOfMeasurement(data.GRAPH_BASE_URI+"unit:" + data.measurementUnit)
                aggregation.hasUnitOfMeasurement=mu
                saoOut.add(mu)
        saoOut.add(interval)
        graph = saopy.RDFInterface.exportRDFGraph(saoOut)
        return graph

# namespaceBindings = {"owl":"http://www.w3.org/2002/07/owl#","sao":"http://purl.oclc.org/NET/UNIS/sao/sao#","vs":"http://www.w3.org/2003/06/sw-vocab-status/ns#","skos":"http://www.w3.org/2004/02/skos/core#","qoi":"http://purl.oclc.org/NET/UASO/qoi#","ct":"http://ict-citypulse.eu/city#","xml":"http://www.w3.org/XML/1998/namespace","owlssc":"http://www.daml.org/services/owl-s/1.2/ServiceCategory.owl#","dc":"http://purl.org/dc/terms/","rdfs":"http://www.w3.org/2000/01/rdf-schema#","wot":"http://xmlns.com/wot/0.1/","owlssp":"http://www.daml.org/services/owl-s/1.2/Profile.owl#","tl":"http://purl.org/NET/c4dm/timeline.owl#","daml":"http://www.daml.org/2001/03/daml+oil#","muo":"http://purl.oclc.org/NET/muo/muo#","foaf":"http://xmlns.com/foaf/0.1/","DUL":"http://www.loa-cnr.it/ontologies/DUL.owl#","time":"http://www.w3.org/2006/time#","dc":"http://purl.org/dc/elements/1.1/","ssn":"http://purl.oclc.org/NET/ssnx/ssn#","ces":"http://www.insight-centre.org/ces#","owlssrp":"http://www.daml.org/services/owl-s/1.2/ServiceParameter.owl#","tzont":"http://www.w3.org/2006/timezone#","geo":"http://www.w3.org/2003/01/geo/wgs84_pos#","owlss":"http://www.daml.org/services/owl-s/1.2/Service.owl#","rdf":"http://www.w3.org/1999/02/22-rdf-syntax-ns#","xsd":"http://www.w3.org/2001/XMLSchema#","prov":"http://www.w3.org/ns/prov#","owlsg":"http://www.daml.org/services/owl-s/1.2/Grounding.owl#"}
