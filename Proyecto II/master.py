from socket import *
import os
import clock

host = "127.0.0.1"  # set to IP address of target computer
buf = 1024
id_host = [3000, 3030, 5000]
process_host = []
UDPSock = socket(AF_INET, SOCK_DGRAM)
addr_self = (host, 4000)
UDPSock.bind(addr_self)

server_time = clock.getTime()

files_slaves = dict()


def berckeley():
    new_time = 0
    for i in id_host:
        address_slave = (host, i)
        UDPSock.sendto("PLEASE TIME", address_slave)
        (time_slave, addr_self) = UDPSock.recvfrom(buf)
        new_time += int(time_slave)

    new_time /= len(id_host)

    for i in id_host:
        address_slave = (host, i)
        UDPSock.sendto("NEW TIME", address_slave)
        UDPSock.sendto(str(new_time), address_slave)

    print clock.toTime(new_time)
    # print (clock.toTime(int(host_rec)))


def filesCopy():
    for i in id_host:
        address_slave = (host, i)
        UDPSock.sendto("FILE", address_slave)
        (size, addr_self) = UDPSock.recvfrom(buf)
        # print size
        for j in range(int(size)):
            (name, addr_self) = UDPSock.recvfrom(buf)
            (content, addr_self) = UDPSock.recvfrom(buf)
            files_slaves[i].append([name, content])


if __name__ == '__main__':
    # berckeley()
    filesCopy()
    print files_slaves

# print(clock.toTime(clock.toSeconds()))

# while process_act < len(process):
#   # addr = (host, i)
#   (host_rec, addr_self) = UDPSock.recvfrom(buf)
#   UDPSock.sendto(str(process[process_act]), (host, int(host_rec)))
#   if host_rec in id_host:
#     print "aqui"
#     ind = id_host.index(host_rec)
#     process_host[ind] = str(process[process_act])
#   else:
#     print "Wlse"
#     id_host.append(host_rec)
#     process_host.append(str(process[process_act]))
#
#   print "____LISTA"
#   for i in range(len(id_host)):
#     print id_host[i] + "-->" + process_host[i]
#   print "____"
#
#   process_act += 1
#
#   # print host_rec

UDPSock.close()
os._exit(0)
