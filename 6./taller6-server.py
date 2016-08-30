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
    x = int(x)
    y = int(y)
    suma = s.suma(x, y)
    server.register_function(suma, 'suma')

def resta_function(x, y):
    x = int(x)
    y = int(y)
    return x - y
server.register_function(resta_function, 'resta')

def multiplicacion_function(x, y):
    x = int(x)
    y = int(y)
    return x * y
server.register_function(multiplicacion_function, 'multiplicacion')

def division_function(x, y):
    x = int(x)
    y = int(y)
    return x / y
server.register_function(division_function, 'division')

def potenciacion_function(x, y):
    x = int(x)
    y = int(y)
    return pow(x, y)
server.register_function(potenciacion_function, 'potenciacion')

def radicacion_function(x, y):
    x = int(x)
    y = float(y)
    c = float(1.0 / y)
    return pow(x, c)
server.register_function(radicacion_function, 'radicacion')

def logaritmo_function(x, y):
    x = int(x)
    y = int(y)
    return log(x, y)
server.register_function(logaritmo_function, 'logaritmo')


# Run the server's main loop
server.serve_forever()
