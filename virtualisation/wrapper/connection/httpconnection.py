__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'

import abstractconnection
import urllib2
from virtualisation.misc.log import Log

class HttpPullConnection(abstractconnection.AbstractConnection):

    def __init__(self, wrapper, source=None):
        super(HttpPullConnection, self).__init__(wrapper)
        self.source = source

    def next(self):
        url = self.source or self.wrapper.getSensorDescription().source
        try:
            return self.load(url)
        except:
            Log.e("HttpPullConnection: failed to load", url)
            return None

    def load(self, url):
        try:
            f = urllib2.urlopen(url, timeout=10)
            r = f.read()
            f.close()
            return r
        except:
            Log.e(self.__class__.__name__, "erro in load")
            return None
