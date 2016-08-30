import os
from socket import *
import math
host = ""
port = 13000
buf = 1024
addr = (host, port)
addr1 = (host, 13001)
addr2 = (host, 13002)
addr3 = (host, 13003)
addr4 = (host, 13004)
addr5 = (host, 13005)
addr6 = (host, 13006)
addr7 = (host, 13007)
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
                (a, addr) = UDPSock.recvfrom(buf)
                (b, addr) = UDPSock.recvfrom(buf)
                UDPSock.sendto(a, addr1)
                UDPSock.sendto(b, addr1)
                (res, addr1) = UDPSock.recvfrom(buf)
            elif (data == "2"):
                (a, addr) = UDPSock.recvfrom(buf)
                (b, addr) = UDPSock.recvfrom(buf)
                UDPSock.sendto(a, addr2)
                UDPSock.sendto(b, addr2)
                (res, addr2) = UDPSock.recvfrom(buf)
            elif (data == "3"):
                (a, addr) = UDPSock.recvfrom(buf)
                (b, addr) = UDPSock.recvfrom(buf)
                UDPSock.sendto(a, addr3)
                UDPSock.sendto(b, addr3)
                (res, addr3) = UDPSock.recvfrom(buf)
            elif (data == "4"):
                (a, addr) = UDPSock.recvfrom(buf)
                (b, addr) = UDPSock.recvfrom(buf)
                UDPSock.sendto(a, addr4)
                UDPSock.sendto(b, addr4)
                (res, addr4) = UDPSock.recvfrom(buf)           
            elif (data == "5"):
                (a, addr) = UDPSock.recvfrom(buf)
                (b, addr) = UDPSock.recvfrom(buf)
                UDPSock.sendto(a, addr5)
                UDPSock.sendto(b, addr5)
                (res, addr5) = UDPSock.recvfrom(buf)           
            elif (data == "6"):
                (a, addr) = UDPSock.recvfrom(buf)
                (b, addr) = UDPSock.recvfrom(buf)
                UDPSock.sendto(a, addr6)
                UDPSock.sendto(b, addr6)
                (res, addr6) = UDPSock.recvfrom(buf)           
            elif (data == "7"):
                (a, addr) = UDPSock.recvfrom(buf)
                (b, addr) = UDPSock.recvfrom(buf)
                UDPSock.sendto(a, addr7)
                UDPSock.sendto(b, addr7)
                (res, addr7) = UDPSock.recvfrom(buf)           

            res= str(res)
            print ("Enviando... " + res)
            UDPSock.sendto(res, addr)

UDPSock.close()
os._exit(0)
