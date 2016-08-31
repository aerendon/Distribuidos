import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler
import math

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server_radicacion = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server_radicacion.register_introspection_functions()

def radicacion_function_server(x, y):
    x = int(x)
    y = float(y)
    c = float(1.0 / y)
    return pow(x, c)
server_radicacion.register_function(radicacion_function_server, 'radicacion_server')

server_radicacion.serve_forever()
