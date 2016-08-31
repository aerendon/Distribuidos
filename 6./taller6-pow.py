import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

server_potenciacion = SimpleXMLRPCServer(("localhost", 8081),requestHandler=RequestHandler)
server_potenciacion.register_introspection_functions()

def potenciacion_function_server(x, y):
    x = int(x)
    y = int(y)
    return pow(x, y)
server_potenciacion.register_function(potenciacion_function_server, 'potenciacion_server')

server_potenciacion.serve_forever()
