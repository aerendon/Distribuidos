import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server_resta = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server_resta.register_introspection_functions()

def resta_function_server(x, y):
    x = int(x)
    y = int(y)
    return x - y
server_resta.register_function(resta_function_server, 'resta_server')

server_resta.serve_forever()
