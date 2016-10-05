import sys
import time
import os
from socket import *

host = "192.168.1.232" # set to IP address of target computer
port1 = 13000
buf = 1024
addr = (host, port1)
UDPSock = socket(AF_INET, SOCK_DGRAM)
UDPSock.bind(addr)
(time2, addr) = UDPSock.recvfrom(buf)
time1 = time.strftime("%H:%M:%S")
UDPSock.sendto(time1, addr)
print ("mi hora " + time1)
print ("hora 2 : " + time2)
UDPSock.close()
os._exit(0)
