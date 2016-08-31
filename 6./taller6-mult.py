import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server_multiplicacion = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server_multiplicacion.register_introspection_functions()

def multiplicacion_function_server(x, y):
    x = int(x)
    y = int(y)
    return x * y
server_multiplicacion.register_function(multiplicacion_function_server, 'multiplicacion_server')

server_multiplicacion.serve_forever()
