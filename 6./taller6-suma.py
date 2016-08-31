import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server_suma = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server_suma.register_introspection_functions()

def suma_function_server(x, y):
    x = int(x)
    y = int(y)
    return x + y
server_suma.register_function(suma_function_server, 'suma_server')

server_suma.serve_forever()
