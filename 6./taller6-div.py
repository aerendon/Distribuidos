import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server_division = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server_division.register_introspection_functions()

def division_function_server(x, y):
    x = int(x)
    y = int(y)
    return x / y
server_division.register_function(division_function_server, 'division_server')

server_division.serve_forever()
