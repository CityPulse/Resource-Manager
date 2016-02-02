
from Queue import Queue, Empty
from time import sleep

import triplestoreadapter
from virtualisation.misc.log import Log as L
from virtualisation.triplestore.sparqlstore import SPARQL_Exception, StoreOffline_Exception
from virtualisation.misc.threads import StoppableThread


__author__ = "Thorben Iggena"

class TripleStoreWriter(StoppableThread):
    
    def __init__(self, queue, bufferSize, graphName, timeout=0.01):
        super(TripleStoreWriter, self).__init__()
        self.buffer = queue
        self.bufferSize = bufferSize
        self.timeout = timeout
        self.graphName = graphName
        self.maxAttempts = 3
    
    def run(self):
        while not self.stopped():
            graphString = ""
            try:
                tmpList = []
                for _ in range(0, self.bufferSize):
                    tmpList.append(self.buffer.get(block=False))
                    self.buffer.task_done()
#                 print "size tmplist", len(tmpList)
            except Empty:
#                 L.d2("Less than", self.bufferSize, "items in queue")
                pass
            finally:
                if len(tmpList) > 0:
#                     L.e("write")
                    graphString = " ".join(tmpList)
                    self.write(graphString)
#                     L.e("write finish")
                if len(tmpList) < self.bufferSize:
                    sleep(self.timeout)

    
    
    def write(self, graphString):
        if ThreadedTriplestoreAdapter.triplestore:
            attempts = self.maxAttempts
            while attempts > 0:
                try:
                    ThreadedTriplestoreAdapter.triplestore.saveMultipleGraphs(graphString, self.graphName)
                    return
                except SPARQL_Exception as e:
#                     self.buffer.put(graphString)
                    attempts -= 1
                    L.e("Error inserting into virtuoso, reattempt")
                except StoreOffline_Exception as e:
                    L.e( "ThreadedTriplestoreAdapter was unable to save data, store might be offline!")
                    break
            #insert some kind of notification that virtuoso insert was not possible




class ThreadedTriplestoreAdapter(object):
    instances = {}
    triplestore = None

    def __new__(cls, graphName, bufferSize=100, maxThreads=4, maxQueueSize=1000):
        if graphName not in ThreadedTriplestoreAdapter.instances:
            ThreadedTriplestoreAdapter.instances[graphName] = ThreadedTriplestoreAdapter.__ThreadedTriplestoreAdapter(graphName,
                                                                                                          bufferSize,
                                                                                                          maxThreads, maxQueueSize)

        return ThreadedTriplestoreAdapter.instances[graphName]

    @classmethod
    def getOrMake(cls, graphName):
        if graphName not in ThreadedTriplestoreAdapter.instances:
            ThreadedTriplestoreAdapter.instances[graphName] = ThreadedTriplestoreAdapter.__ThreadedTriplestoreAdapter(graphName)
        return ThreadedTriplestoreAdapter.instances[graphName]
    
    @classmethod
    def getTotalBufferSize(cls):
        bufferSize = 0
        for graphName in ThreadedTriplestoreAdapter.instances:
            bufferSize += ThreadedTriplestoreAdapter.instances[graphName].getBufferSize()
        return bufferSize
    
    @classmethod
    def stop(cls):
        for graphName in ThreadedTriplestoreAdapter.instances:
            while ThreadedTriplestoreAdapter.instances[graphName].getBufferSize() != 0:
                sleep(0.001)
            ThreadedTriplestoreAdapter.instances[graphName].stopWriterThreads()

    class __ThreadedTriplestoreAdapter(triplestoreadapter.TripleStoreAdapter):
        def __init__(self, graphName, bufferSize=100, maxThreads=4, maxQueueSize=1000):
            self.graphName = graphName
            self.buffer = Queue(maxQueueSize)
            self.timer = None
            self.threads = []
            self.maxThreads = maxThreads
            self.bufferSize = bufferSize
            self.startWriterThreads()
            
        def stopWriterThreads(self):
            for t in self.threads:
                t.stop()
            
        def startWriterThreads(self):
            for i in range(self.maxThreads):
                t = TripleStoreWriter(self.buffer, self.bufferSize, self.graphName)
                t.start()
                self.threads.append(t)

        def addSerialisedGraph(self, serialisedGraph):
            for line in serialisedGraph.split("\n"):
                self.buffer.put(line)
            
        def getBufferSize(self):
            return self.buffer.qsize()

        def addGraph(self, graph):
            self.addSerialisedGraph(graph.serialize(destination=None, format='nt', encoding=None))

        def addGraphList(self, graphList):
            for graph in graphList:
                self.addGraph(graph)





        def saveGraphAsync(self, graph=None, graphName=None):
            self.addGraph(graph)

        def createGraph(self, graphName):
            return ThreadedTriplestoreAdapter.triplestore.createGraph(graphName)

        def saveTriple(self, graphName, subject, predicate, _object):
            ThreadedTriplestoreAdapter.triplestore.saveTriple(graphName, subject, predicate, _object)

        def saveGraph(self, graph=None, graphName=None):
            ThreadedTriplestoreAdapter.triplestore.saveGraph(graph, graphName)

        # def getAllSensorObservations(self, propertyType, serviceCategoryName):
        #     return ThreadedTriplestoreAdapter.triplestore.getAllSensorObservations(propertyType, serviceCategoryName)
        
        def deleteGraph(self, graphName):
            ThreadedTriplestoreAdapter.triplestore.deleteGraph(graphName)

        def graphExists(self, graphName):
            return ThreadedTriplestoreAdapter.triplestore.graphExists(graphName)

        def saveMultipleGraphs(self, serialisedGraph, graphName=None):
            ThreadedTriplestoreAdapter.triplestore.saveMultipleGraphs(serialisedGraph, graphName)

        def getObservationGraph(self, graphName, sensor, start=None, end=None, asGraph=True):
            ThreadedTriplestoreAdapter.triplestore.getObservationGraph(graphName, sensor, start, end, asGraph)
        
        def getLastQoIData_List(self, graphName, sensorName):
            ThreadedTriplestoreAdapter.triplestore.getLastQoIData_List(graphName, sensorName)

        def getStreamMinMaxDate(self, graphName, sensorName):
            ThreadedTriplestoreAdapter.triplestore.getStreamMinMaxDate(graphName, sensorName)