import os
import xmlrpclib
from SimpleXMLRPCServer import SimpleXMLRPCServer
from SimpleXMLRPCServer import SimpleXMLRPCRequestHandler

s = xmlrpclib.ServerProxy('http://localhost:8081')

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
server = SimpleXMLRPCServer(("localhost", 8000),requestHandler=RequestHandler)
server.register_introspection_functions()

# Register a function under a different name
def suma_function(x, y):
    suma = s.suma_server(x, y)
    return suma
server.register_function(suma_function, 'suma')

def resta_function(x, y):
    resta = s.resta_server(x, y)
    return resta
server.register_function(resta_function, 'resta')

def multiplicacion_function(x, y):
    multiplicacion = s.multiplicacion_server(x, y)
    return multiplicacion
server.register_function(multiplicacion_function, 'multiplicacion')

def division_function(x, y):
    division = s.division_server(x, y)
    return division
server.register_function(division_function, 'division')

def potenciacion_function(x, y):
    potenciacion = s.potenciacion_server(x, y)
    return potenciacion
server.register_function(potenciacion_function, 'potenciacion')

def radicacion_function(x, y):
    radicacion = s.radicacion_server(x, y)
    return radicacion
server.register_function(radicacion_function, 'radicacion')

def logaritmo_function(x, y):
    logaritmo = s.logaritmo_server(x, y)
    return logaritmo
server.register_function(logaritmo_function, 'logaritmo')


# Run the server's main loop
server.serve_forever()
