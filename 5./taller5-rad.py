import os
from socket import *
import math
host = ""
port = 13006
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting to receive messages..."
while True:
      (a, addr) = UDPSock.recvfrom(buf)
      (b, addr) = UDPSock.recvfrom(buf)
      a = float(a)
      b = float(b)
      c = 1.0 / b
      res = math.pow(a,c)
      res = str(res)
      print ("Enviando... " + res)
      UDPSock.sendto(res, addr)

UDPSock.close()
os._exit(0)

