import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server_logaritmo = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server_logaritmo.register_introspection_functions()

def logaritmo_function_server(x, y):
    x = int(x)
    y = int(y)
    return math.log(x, y)
server_logaritmo.register_function(logaritmo_function_server, 'logaritmo_server')

server_logaritmo.serve_forever()
