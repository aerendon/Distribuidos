import os
from socket import *
import math
host = "192.168.8.63"
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
         archivo=open('texto.txt','r')
         archivo=archivo.read()
         cont=0
         for i in archivo:
             if data == i:
               cont= cont + 1
               print cont
         res= cont
         print res
         res = str(res)
         print ("Enviando... " + res)
         UDPSock.sendto(res, addr)

UDPSock.close()
os._exit(0)
