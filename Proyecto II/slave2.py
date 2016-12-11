import sys
import time
import os
import clock
from socket import *

host = "127.0.0.1" # set to IP address of target computer
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)

addr_self = (host, 5000)
UDPSock.bind(addr_self)

addr_server = (host, 4000)

time_slave = clock.toSeconds()

def berckeley():
    (host_rec, addr_self) = UDPSock.recvfrom(buf)
    if host_rec == "PLEASE TIME":
        UDPSock.sendto(str(time_slave), addr_server)

    (host_rec, addr_self) = UDPSock.recvfrom(buf)
    if host_rec == "NEW TIME":
        (new_time, addr_self) = UDPSock.recvfrom(buf)
        return int(new_time)


    #
    # print time_slave

if __name__ == '__main__':
    time_slave = clock.toTime(berckeley())
    print time_slave


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
