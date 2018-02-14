from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler
from scipy import stats

class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)


server = SimpleXMLRPCServer(("10.211.55.2", 8000),
                            requestHandler=RequestHandler)
server.register_introspection_functions()



def betaPDF(x,a,b):
     print(stats.beta.pdf(x,a,b).item())
     return stats.beta.pdf(x,a,b).item()
server.register_function(betaPDF, 'betaPDF')


server.serve_forever()