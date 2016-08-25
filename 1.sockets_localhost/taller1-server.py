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
            (a, addr) = UDPSock.recvfrom(buf)
            (b, addr) = UDPSock.recvfrom(buf)
            a = float(a)
            b = float(b)

            if (data == "1"):
                res = a + b
            elif (data == "2"):
                res = a - b
            elif (data == "3"):
                res = a * b
            elif (data == "4"):
                res = a / b
            elif (data == "5"):
                res = math.pow(a, b)
            elif (data == "6"):
                c = 1.0/ b
                res = math.pow(a , c )
            elif (data == "7"):
                res = math.log(a, b)

            res = str(res)
            print ("Enviando... " + res)
            UDPSock.sendto(res, addr)

UDPSock.close()
os._exit(0)
