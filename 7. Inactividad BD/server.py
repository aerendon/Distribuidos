import sys
import time
import os
from socket import *

host = "127.0.0.1" # set to IP address of target computer
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)
addr_self = (host, 4000)
UDPSock.bind(addr_self)


# (id_rec, addr_self) = UDPSock.recvfrom(buf)
# (host_rec, addr_self) = UDPSock.recvfrom(buf)
# addr = (host, int(host_rec))
# print (addr)
# UDPSock.sendto (str(max(int(id_host), int(id_rec))), addr)
# print ("id " + str(max(int(id_host), int(id_rec)))+ " enviado...")

UDPSock.close()
os._exit(0)
