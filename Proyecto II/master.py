#!/usr/bin/python
import time
from socket import *
import os
import clock
import random

host = "127.0.0.1"  # set to IP address of target computer
buf = 1024
id_host = [3000, 3030, 5000]
process_host = []
UDPSock = socket(AF_INET, SOCK_DGRAM)
addr_self = (host, 4000)
UDPSock.bind(addr_self)

server_time = clock.getTime()

files_slaves = {}
copy_files_slaves = {}


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

    print (clock.toTime(int(host_rec)))


def filesCopy():
    for i in id_host:
        # print "Slave search" + str(i)
        address_slave = (host, i)
        UDPSock.sendto("FILE", address_slave)
        (size, addr_self) = UDPSock.recvfrom(buf)
        files_slaves[i] = []
        # print size
        for __ in range(int(size)):
            # (name, addr_self) = UDPSock.recvfrom(buf)
            # print name
            (name, addr_self) = UDPSock.recvfrom(buf)
            (content, addr_self) = UDPSock.recvfrom(buf)
            files_slaves[i].append([str(i) + name, content])

        # print "slave " + str(i) +" files"
        # print files_slaves[i]


def randomServer(init, end):
    new = random.randint(init, end)
    return new


def makeCopy():
    for copies in files_slaves:
        # print files_slaves[copies]
        files = files_slaves[copies]
        for name, content in files:
            copy_files_slaves[name] = []
            # print copies
            # print name

            copy = randomServer(0, len(id_host) - 1)
            while(id_host[copy] == copies):
                copy = randomServer(0, len(id_host) - 1)
            # print str(copies) + "Se va para -> " + str(copy)
            copy_files_slaves[name].append([id_host[copy], content])


def sendCopy():
    for copies in copy_files_slaves:
        # print copy_files_slaves[copies]
        port, content = copy_files_slaves[copies][0]
        address_slave = (host, port)
        UDPSock.sendto("LOOP", address_slave)
        UDPSock.sendto(copies, address_slave)
        UDPSock.sendto(content, address_slave)

    for port in id_host:
        address_slave = (host, port)
        UDPSock.sendto("FINISH", address_slave)


def updateFiles(port, name, content):
    for server in files_slaves:
        for i in range(len(files_slaves[server]) - 1):
            # print server
            if files_slaves[server][i][0] == (port + name):
                files_slaves[server][i][1] = content

def check():
    for port in id_host:
        address_slave = (host, port)
        # print len(files_slaves[port])
        for __ in range(len(files_slaves[port])):
            (confirmation, addr_self) = UDPSock.recvfrom(buf)
            if confirmation == "CHANGE":

                (port_server, addr_self) = UDPSock.recvfrom(buf)
                (path, addr_self) = UDPSock.recvfrom(buf)
                (content, addr_self) = UDPSock.recvfrom(buf)
                updateFiles(port_server, path, content)
                return True


if __name__ == '__main__':
    while True:
        for port in id_host:
            address_slave = (host, port)
            UDPSock.sendto("OK", address_slave)

        filesCopy()
        makeCopy()
        sendCopy()
        # print copy_files_slaves
        if check():
            berckeley()
            print "SI"
        time.sleep(5)

UDPSock.close()
os._exit(0)
