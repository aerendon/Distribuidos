import os
from socket import *
import math
host = ""
port = 13000
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
        if int(data) < 1 or int(data) > 6:
            print ("Opcion no valida")
        else:

            if (data == "1"):
                res = "13001,13002,13003"
            elif (data == "2"):
                res = "13001,13002,13003"
            elif (data == "3"):
                res = "13001,13002,13003"
            elif (data == "4"):
                res = "13001,13002,13003"
            elif (data == "5"):
                rres = "13001,13002,13003"
            elif (data == "6"):
                res = "13001,13002,13003"
            elif (data == "7"):
                res = "13001,13002,13003"
            res = str(res)
            print ("Enviando... " + res)
            UDPSock.sendto(res, addr)

UDPSock.close()
os._exit(0)
