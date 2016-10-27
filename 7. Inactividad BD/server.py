import sys
import time
import os
from socket import *

host = "127.0.0.1" # set to IP address of target computer
buf = 1024
id_host = []
process_host = []
UDPSock = socket(AF_INET, SOCK_DGRAM)
addr_self = (host, 4000)
UDPSock.bind(addr_self)

process = [10, 2, 5, 15, 3, 7, 8, 1]
process_act = 0

while process_act < len(process):
  # addr = (host, i)
  (host_rec, addr_self) = UDPSock.recvfrom(buf)
  UDPSock.sendto(str(process[process_act]), (host, int(host_rec)))
  if host_rec in id_host:
    print "aqui"
    ind = id_host.index(host_rec)
    process_host[ind] = str(process[process_act])
  else:
    print "Wlse"
    id_host.append(host_rec)
    process_host.append(str(process[process_act]))

  print "____LISTA"
  for i in range(len(id_host)):
    print id_host[i] + "-->" + process_host[i]
  print "____"

  process_act += 1

  # print host_rec

UDPSock.close()
os._exit(0)
