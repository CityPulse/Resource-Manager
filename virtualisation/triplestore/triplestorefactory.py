__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

from sparqlstore import SparqlStore
from fusekistore import FusekiStore

class TripleStoreFactory(object):
    __classes = { "sparql": SparqlStore, "fuseki": FusekiStore }

    @classmethod
    def getTripleStore(cls, driver, triplestoreconfiguration):
        if driver not in TripleStoreFactory.__classes:
            raise Exception("Triplestore driver unknown")

        return TripleStoreFactory.__classes[driver](triplestoreconfiguration)
