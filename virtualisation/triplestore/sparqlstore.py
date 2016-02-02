from os.path import os
import threading
from urllib2 import HTTPError
import urllib2

from SPARQLWrapper import SPARQLWrapper, POST, JSON, SELECT
from rdflib.graph import ConjunctiveGraph

import triplestoreadapter
from virtualisation.misc.jsonobject import JSONObject
from virtualisation.misc.log import Log as L
from SPARQLWrapper.SPARQLExceptions import EndPointInternalError,\
    EndPointNotFound

__author__ = 'sefki'
__author__ = "thiggena"

class SPARQL_Exception(Exception):
    pass

class StoreOffline_Exception(Exception):
    pass

class SparqlStore(triplestoreadapter.TripleStoreAdapter):
    SPARQL_ENDPOINT = None
    GRAPH_BASE_URI = None

    def __init__(self, triplestoreconfiguration):
        if not SparqlStore.SPARQL_ENDPOINT:
            SparqlStore.SPARQL_ENDPOINT = "http://%s:%d/" % (triplestoreconfiguration.host, triplestoreconfiguration.port)
            if "path" in triplestoreconfiguration:
                SparqlStore.SPARQL_ENDPOINT += triplestoreconfiguration.path
        if not SparqlStore.GRAPH_BASE_URI:
            SparqlStore.GRAPH_BASE_URI = triplestoreconfiguration.base_uri

        self.dictIDs = {}

    # prepares the SPARQL wrapper object
    def getSparqlObject(self, graphName=None, query=None):
        sparql = SPARQLWrapper(SparqlStore.SPARQL_ENDPOINT)
        sparql.addDefaultGraph(self.getGraphURI(graphName))
        sparql.setQuery(query)
        sparql.setMethod(POST)
        sparql.queryType = SELECT
        sparql.setReturnFormat(JSON)
        sparql.setTimeout(0.1)
        return sparql

    # deletes unusable characters within URI
    def getGraphURI(self, graphName, prependBase=True):
        if prependBase:
            graphURI = SparqlStore.GRAPH_BASE_URI + graphName
        else:
            graphURI = graphName
        return urllib2.quote(graphURI, "://#")

    # returns if graph doesn't exist or is empty(!)
    # there is no possibility to check for existing but empty graphs
    def graphExists(self, graphName):
        queryString = "ASK { GRAPH <" + self.getGraphURI(graphName) + "> { ?s ?p ?o . }}"
        sparql = self.getSparqlObject(graphName, queryString)
        # print queryString
        try:
            ret = sparql.query()
            retList = ret.convert()
            #             print retList
            return retList["boolean"]
        except HTTPError as e:
            L.e("Sparql Endpoint HTTPError in graphExists:", str(e.code), e.reason)
        except Exception as e:
            L.e("Error in graphExists:", e.message)

    # creates an empty graph for the new dataset
    def createGraph(self, graphName):
        queryString = "CREATE GRAPH <" + self.getGraphURI(graphName) + ">"
        sparql = self.getSparqlObject(graphName, queryString)
        try:
            ret = sparql.query().convert()
            return True
        except HTTPError as e:
            L.e("Sparql Endpoint HTTPError in createGraph:", str(e.code), e.reason)
        except Exception as e:
            L.e("Error in createGraph:", e.message)
            return False

    def saveTriple(self, graphName, subject, predicate, object):
        sparql = self.getSparqlObject(graphName)
        # insert into doesn't work with set default graph, have to "... INSERT DATA INTO <graph>..."
        queryString = "INSERT DATA INTO <" + self.getGraphURI(
            graphName) + "> { <" + subject + "> <" + predicate + "> <" + object + "> }"
        sparql.setQuery(queryString)
        try:
            sparql.query()
        except HTTPError as e:
            L.e("Sparql Endpoint HTTPError in saveTriple:", str(e.code), e.reason)
        except Exception as e:
            L.e("Error in saveTriple:", e.message)

    def saveGraph(self, graph, graphName):
        serialisation = graph.serialize(destination=None, format='nt', encoding=None)
        queryString = "".join(["INSERT DATA INTO GRAPH <", self.getGraphURI(graphName), "> {", serialisation, "}"])
        sparql = self.getSparqlObject(graphName, queryString)
        try:
            sparql.query()
        except HTTPError as e:
            L.e("Sparql Endpoint HTTPError in saveGraph:", str(e.code), e.reason)
        except Exception as e:
            L.e("Error in saveGraph:", e.message)

    def saveGraphAsync(self, graph=None, graphName=None):
        threading.Thread(target=self.saveGraph, args=(graph, graphName)).start()

    def saveMultipleGraphs(self, serialisedGraph, graphName=None):
        queryString = "".join(["INSERT DATA INTO GRAPH <", self.getGraphURI(graphName), "> {", serialisedGraph, "}"])
        sparql = self.getSparqlObject(graphName, queryString)
        try:
            ret = sparql.query()
        except EndPointInternalError as e:  #transaction deadlock case
            L.e("Error in saveMultipleGraphs:", e.message)
            raise SPARQL_Exception()
            L.e("Error in saveMultipleGraphs:", e.message)
        except EndPointNotFound as e:   #temporarily 404 error
            L.e("Error in saveMultipleGraphs:", e.message)
            raise SPARQL_Exception()
        except Exception as e:
            L.e("Error in saveMultipleGraphs:", e.message)
            raise StoreOffline_Exception()

    def getObservationGraph(self, graphName, sensor, start = None, end = None, asGraph=True):
        dateFilter = ""
        if start and end:
            dateFilter = "FILTER (   (xsd:dateTime(?resultTimeValue) >= xsd:dateTime(\"" + start + "\"))   &&    (xsd:dateTime(?resultTimeValue) <= xsd:dateTime(\"" + end + "\"))   ) "       
        elif start:
            dateFilter = "FILTER (   (xsd:dateTime(?resultTimeValue) >= xsd:dateTime(\"" + start + "\")) ) "         
            
        queryString = """DEFINE sql:log-enable 2 prefix : <http://stefan.com/>
                            prefix sao: <http://purl.oclc.org/NET/UNIS/sao/sao#> 
                            prefix ssn: <http://purl.oclc.org/NET/ssnx/ssn#> 
                            prefix tl: <http://purl.org/NET/c4dm/timeline.owl#> 
                            
                            CONSTRUCT {?s ?p ?o}
                            where {
                              {
                                ?observation (!:)* ?s .
                                ?s ?p ?o .
                              }
                            {
                            ?observation a sao:Point.
                            ?observation ssn:observationResultTime ?resultTime .
                            ?resultTime tl:at ?resultTimeValue .
                            ?observation ssn:observedBy <""" + sensor + """> .""" + dateFilter + """}}"""
                         
        sparql = self.getSparqlObject(graphName, queryString)
        sparql.setReturnFormat("n3")
        try:
            ret = sparql.query().convert()
            if not asGraph:
                return ret
            else:
                g = ConjunctiveGraph()
                return g.parse(data=ret, format="n3")
        except Exception as e:
            L.e("Error in getObservationGraph:", e.message)
            return None

    def deleteGraph(self, graphName):
        queryString = "DEFINE sql:log-enable 3 DROP SILENT GRAPH <" + self.getGraphURI(graphName) + ">"
        L.d("deleteGraph using query:", queryString)
        sparql = self.getSparqlObject(graphName, queryString)
        sparql.setTimeout(300)
        try:
            ret = sparql.query()
            return True
        except Exception as e:
            L.e("Error in deleteGraph:", e.message)
            return False
                   
    #sensorNames have to be in the same graph!
    def getLastQoIData_List(self, graphName, sensorNames, start=None, end=None):      
        length = len(sensorNames)
        i = 1
        sensorFilter = "FILTER("                    
        for sensor in sensorNames:
            if i < length:
                sensorFilter = "".join([sensorFilter, "?sensor = <", sensor, "> || "])
            else:
                sensorFilter = "".join([sensorFilter, "?sensor = <", sensor, "> )"])
            i += 1
            
        dateFilter = ""
        limit = ""
        if start and end:
            dateFilter = "FILTER (   (xsd:dateTime(?resultTimeValue) >= xsd:dateTime(\"" + start + "\"))   &&    (xsd:dateTime(?resultTimeValue) <= xsd:dateTime(\"" + end + "\"))   ) "       
        elif start:
            dateFilter = "FILTER (   (xsd:dateTime(?resultTimeValue) >= xsd:dateTime(\"" + start + "\")) ) "
        else:
            limit = "LIMIT " + str(length)
                        
        queryString = """prefix ssn: <http://purl.oclc.org/NET/ssnx/ssn#> prefix tl: <http://purl.org/NET/c4dm/timeline.owl#> 
                         prefix sao: <http://purl.oclc.org/NET/UNIS/sao/sao#> 
                         prefix ces: <http://www.insight-centre.org/ces#> prefix so: <http://www.daml.org/services/owl-s/1.2/Service.owl#> 
                         prefix qoi: <http://purl.oclc.org/NET/UASO/qoi#> 
                         prefix prov: <http://www.w3.org/ns/prov#> 
                         SELECT 
                         distinct(?sensor) ?absoluteAge ?ratedAge ?unitAge ?absoluteCompleteness ?ratedCompleteness ?unitCompleteness 
                         ?absoluteCorrectness ?ratedCorrectness ?unitCorrectness ?absoluteFrequency ?ratedFrequency ?unitFrequency 
                         ?absoluteLatency ?ratedLatency ?unitLatency ?resultTimeValue
                         WHERE { 
                            ?quality1 qoi:hasAbsoluteQuality ?absoluteAge .
                            ?quality1 qoi:hasRatedQuality ?ratedAge .
                            ?quality1 qoi:hasUnitOfMeasurement ?unitAge .
                            ?quality2 qoi:hasAbsoluteQuality ?absoluteCompleteness .
                            ?quality2 qoi:hasRatedQuality ?ratedCompleteness .
                            ?quality2 qoi:hasUnitOfMeasurement ?unitCompleteness .
                            ?quality3 qoi:hasAbsoluteQuality ?absoluteCorrectness .
                            ?quality3 qoi:hasRatedQuality ?ratedCorrectness .
                            ?quality3 qoi:hasUnitOfMeasurement ?unitCorrectness .
                            ?quality4 qoi:hasAbsoluteQuality ?absoluteFrequency .
                            ?quality4 qoi:hasRatedQuality ?ratedFrequency .
                            ?quality4 qoi:hasUnitOfMeasurement ?unitFrequency .
                            ?quality5 qoi:hasAbsoluteQuality ?absoluteLatency .
                            ?quality5 qoi:hasRatedQuality ?ratedLatency .
                            ?quality5 qoi:hasUnitOfMeasurement ?unitLatency .

                            ?quality1 a qoi:Age .
                            ?quality2 a qoi:Completeness .
                            ?quality3 a qoi:Correctness .
                            ?quality4 a qoi:Frequency .
                            ?quality5 a qoi:Latency .
                            ?observation qoi:hasQuality ?quality1 . 
                            ?observation qoi:hasQuality ?quality2 . 
                            ?observation qoi:hasQuality ?quality3 . 
                            ?observation qoi:hasQuality ?quality4 . 
                            ?observation qoi:hasQuality ?quality5 . 
                            ?observation ssn:observationResultTime ?time . 
                            ?observation ssn:observedBy ?sensor . 
                            ?time tl:at ?resultTimeValue . """ + sensorFilter + " " + dateFilter + """
                            } ORDER BY DESC(?resultTimeValue) """ + limit
        sparql = self.getSparqlObject(graphName, queryString)
        try:
            ret = sparql.query().convert()
            return ret
        except Exception as e:
            L.e("Error in getQoIData:", e.message)
    
    def getStreamMinMaxDate(self, graphName, sensorName):
        queryString = """prefix ssn: <http://purl.oclc.org/NET/ssnx/ssn#> prefix tl: <http://purl.org/NET/c4dm/timeline.owl#> 
                        prefix sao: <http://purl.oclc.org/NET/UNIS/sao/sao#> prefix ces: <http://www.insight-centre.org/ces#> 
                        prefix so: <http://www.daml.org/services/owl-s/1.2/Service.owl#> prefix qoi: <http://purl.oclc.org/NET/UASO/qoi#> 
                        prefix prov: <http://www.w3.org/ns/prov#> 
                        SELECT   MAX(str(?timeValue)) as ?maxDateTime MIN(str(?timeValue)) as ?minDateTime 
                        WHERE { ?observation ssn:observationResultTime ?time . ?observation ssn:observedBy <""" + sensorName + """> . ?time tl:at ?timeValue .  }"""

        sparql = self.getSparqlObject(graphName, queryString)
        try:
            ret = sparql.query().convert()
            return ret
        except Exception as e:
            L.e("Error in getStreamMinMaxDate:", e.message)


if __name__ == '__main__':
    from virtualisation.triplestore.triplestorefactory import TripleStoreFactory
    config = JSONObject(file(os.path.join(os.path.dirname(__file__), "..", "config.json"), "rb"))
    tripleStore = TripleStoreFactory.getTripleStore(config.triplestore.driver, config.triplestore)
    
#     x = JSONObject()
# 
    print tripleStore.getObservationGraph2("aarhus_road_parking#", "http://ict-citypulse.eu/SensorID-9ae902fb-232b-5ea8-b7be-34d60d563112", "2015-10-09T17:27:38", "2015-10-10T17:29:28", asGraph=False)
#     print x.dumps()

#     sensorNames = ["http://ict-citypulse.eu/SensorID-4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f", "http://ict-citypulse.eu/SensorID-d281e004-dfac-56c4-b237-d3b854c63558", \
#                    "http://ict-citypulse.eu/SensorID-4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f", "http://ict-citypulse.eu/SensorID-4ebf0933-b115-5e44-98e7-2432325395a1", \
#                    "http://ict-citypulse.eu/SensorID-2586bf63-d256-59a0-bc29-9d04eb92dacb", "http://ict-citypulse.eu/SensorID-fb6c280f-1daa-56ea-a984-bfc2ae79d835", \
#                    "http://ict-citypulse.eu/SensorID-51f0f28c-0909-5a83-a310-b6bd686bf57b", "http://ict-citypulse.eu/SensorID-d281e004-dfac-56c4-b237-d3b854c63558"]
#     sensorNames = ["http://ict-citypulse.eu/SensorID-4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f"]
# 
# 
#     import datetime
    
#     for _i in range(0,2):
#         tstart = datetime.datetime.now()
#         for sensor in sensorNames:
#             tripleStore.getLastQoIData("aarhus_road_parking#", sensor)
#         print "Testing time for getLastQoIData:", (datetime.datetime.now() - tstart).total_seconds()        
            
#     tstart = datetime.datetime.now()
#     print tripleStore.getLastQoIData_List("aarhus_road_parking#", sensorNames, "2016-10-13T13:40:01", "2015-10-13T13:42:01")
#     print "Testing time for getLastQoIData2:", (datetime.datetime.now() - tstart).total_seconds()  
    
    
    
    
    
    
#     print tripleStore.getQoIData("aarhus_road_parking#", "http://ict-citypulse.eu/SensorID-0816d088-3af8-540e-b89b-d99ac63fa886", "2015-10-08T10:35:01", "2015-10-08T10:40:01")
    

#     tripleStore.createGraph("test")
#     tripleStore.deleteGraph("test")
#     tripleStore.createGraph("test")
#     tripleStore.deleteGraph("test")
#     tripleStore.createGraph("test2")
#     tripleStore.deleteGraph("test2")
#     tripleStore.createGraph("test")
#     import datetime
#     tstart = datetime.datetime.now()
#     tripleStore.deleteGraph("aarhus_road_traffic#") 
#     print "Testing timeout for delete TIME:", (datetime.datetime.now() - tstart).total_seconds()
    
#     print tripleStore.getLastQoIData("aarhus_road_parking#", "http://ict-citypulse.eu/SensorID-4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f")
#     print tripleStore.getQoIData("aarhus_road_parking#", "http://ict-citypulse.eu/SensorID-4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f", start="2015-09-01T10:42:50", end="2015-09-01T11:42:55")
# 
#     print tripleStore.getStreamMinMaxDate("aarhus_road_parking#", "http://ict-citypulse.eu/SensorID-4a838c4b-30d0-5fb4-b3b5-16d6c5c4ff9f")
