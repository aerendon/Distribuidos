import os
from socket import *
import math
host = ""
port = 13001
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
print "Waiting to receive messages..."
while True:
    (data, addr) = UDPSock.recvfrom(buf)
    print "Received message: " + data
    if data == "exit":
        break
    else:
          (a, addr) = UDPSock.recvfrom(buf)
          (b, addr) = UDPSock.recvfrom(buf)
          a = float(a)
          b = float(b)

          if (data == "1"):
              resop = a + b
          elif (data == "2"):
              resop = a - b
          elif (data == "3"):
              resop = a * b
          elif (data == "4"):
              resop = a / b
          elif (data == "5"):
              res = math.pow(a, b)
          elif (data == "6"):
              c = 1.0/ b
              resop = math.pow(a , c )
          elif (data == "7"):
              resop = math.log(a, b)

          resop = str(resop)
          print ("Enviando... " + resop)
          UDPSock.sendto(resop, addr)

UDPSock.close()
os._exit(0)
