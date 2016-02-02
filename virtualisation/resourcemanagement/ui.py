import cherrypy

__author__ = 'Marten Fischer (m.fischer@hs-osnabrueck.de)'


class Ui(object):

    def __init__(self, resourcemanagement):
        self.rm = resourcemanagement

    @cherrypy.expose
    def index(self):
        return "No UI available yet!"

    @cherrypy.expose
    def deploy(self):
        return """
            <html><body>
                <form method="POST" action="/api/deploy" enctype="multipart/form-data">
                    <input type="file" name="deployunit">
                    <input type="submit" value="send">
                </form>
            </body></html>
        """

    @cherrypy.expose
    def overview(self):
        yield '<html><body><table style="border: 1px solid grey;">'
        sds = []
        for w in self.rm.wrappers:
            if not isinstance(w.getSensorDescription(), list):
                sds += [w.getSensorDescription()]
            else:
                sds += w.getSensorDescription()
        for sd in sds:
            yield '<tr><td>%(uuid)s</td><td>%(sensorID)s</td>' \
                  '<td>%(sensorType)s</td><td>%(sensorName)s</td>' \
                  '<td>%(author)s</td><td>%(information)s</td>' \
                  '<td><a href="/api/remove_wrapper?uuid=%(uuid)s">remove</a></td>' \
                  '<td><a href="/api/get_description?uuid=%(uuid)s" target="_blank">get_description</a></td>' \
                  '<td><a href="/api/snapshot?uuid=%(uuid)s" target="_blank">snapshot</a></td>' \
                  '<td><a href="/api/snapshot_sql?uuid=%(uuid)s" target="_blank">snapshot_sql</a></td>' \
                  '<td><a href="/api/get_static_stream_data?uuid=%(uuid)s" target="_blank">static_data</a></td>' \
                  '<td><a href="/api/data_timeframe?uuid=%(uuid)s" target="_blank">timeframe</a><a href="/api/data_timeframe_sql?uuid=%(uuid)s" target="_blank">sql</a></td></tr>' % sd
        yield '</table></body></html>'
        return