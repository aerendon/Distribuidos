import sys
import time
import os
from socket import *

host = "127.0.0.1" # set to IP address of target computer
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)

addr_self = (host, 3000)
UDPSock.bind(addr_self)

addr_server = (host, 4000)
# signal = "1"
#
# while True:
#   UDPSock.sendto("3000", addr_server)
#   (process, addr_self) = UDPSock.recvfrom(buf)
#   print "Tiene un proceso de " + process + "Seg"
#
#   time.sleep(int(process))
#


UDPSock.close()
os._exit(0)
