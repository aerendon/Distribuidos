import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

server = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server.register_introspection_functions()

def suma_function(x, y):
    x = int(x)
    y = int(y)
    return x + y
server.register_function(suma_function, 'suma')

server.serve_forever()
