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

files_slaves = {}


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
        print "Slave search" + str(i)
        address_slave = (host, i)
        UDPSock.sendto("FILE", address_slave)
        (size, addr_self) = UDPSock.recvfrom(buf)
        files_slaves[i] = []
        print size
        for __ in range(int(size)):
            # (name, addr_self) = UDPSock.recvfrom(buf)
            # print name
            (name, addr_self) = UDPSock.recvfrom(buf)
            (content, addr_self) = UDPSock.recvfrom(buf)
            files_slaves[i].append([name, content])

        print "slave " + str(i) +" files"
        print files_slaves[i]

if __name__ == '__main__':
    # berckeley()
    filesCopy()
    # print files_slaves


UDPSock.close()
os._exit(0)
