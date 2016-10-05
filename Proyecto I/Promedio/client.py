import sys
import time
import os
from socket import *

host = "127.0.0.1" # set to IP address of target computer
port1 = 13000
port2 = 13001
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
    else:
        if int(data) < 1 or int(data) > 7:
            print ("Opcion no valida")
        else:
            a = raw_input("A : ")
            b = raw_input("B : ")
            UDPSock.sendto(a, addr)
            UDPSock.sendto(b, addr)
            (res, addr) = UDPSock.recvfrom(buf)
            print ("resultado : " + res)
UDPSock.close()
os._exit(0)
