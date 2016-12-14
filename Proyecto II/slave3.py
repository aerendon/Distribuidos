import sys
import time
import os
import clock
from socket import *
import glob

host = "127.0.0.1" # set to IP address of target computer
buf = 1024
UDPSock = socket(AF_INET, SOCK_DGRAM)
addr_self = (host, 3030)
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


def files():
    return glob.glob("*.txt")


def contentFiles(files):
    content_files = []
    for i in files:
        content = open(i, 'r')
        # print content.read()
        content_files.append([i, content.read()])
        content.close()

    return content_files


def filesCopy():
    slaveFiles = files()
    files_str = contentFiles(slaveFiles)
    (message, addr_self) = UDPSock.recvfrom(buf)
    if message == "FILE":
        UDPSock.sendto(str(len(files_str)), addr_server)
        # print files_str
        for name, content in files_str:
            # UDPSock.sendto("ARCHIVO", addr_server)
            UDPSock.sendto(name, addr_server)
            UDPSock.sendto(content, addr_server)


def createFile(path, content):
    if os.path.exists(path):
        f = file(path + ".copy", "r+")
    else:
        f = file(path + ".copy", "w")

    f.write(content)

def recieveCopy():
    while True:
        (init, addr_self) = UDPSock.recvfrom(buf)
        if init == "FINISH":
            break
        else:
            (name, addr_self) = UDPSock.recvfrom(buf)
            (content, addr_self) = UDPSock.recvfrom(buf)
            print name
            print content
            createFile(name, content)


def check(server_files):
    server_files_now = contentFiles(files())
    for i in range(len(server_files)):
        if server_files[i][0] == server_files_now[i][0] and server_files[i][1] == server_files_now[i][1]:
            UDPSock.sendto("OK", addr_server)
        else:
            UDPSock.sendto("CHANGE", addr_server)
            UDPSock.sendto("3030", addr_server)
            UDPSock.sendto(server_files_now[i][0], addr_server)
            UDPSock.sendto(server_files_now[i][1], addr_server)

if __name__ == '__main__':
    # slaveFiles = files()
    while True:
        # time_slave = clock.toTime(berckeley())
        # print time_slave
        server_files = contentFiles(files())
        print server_files
        filesCopy()
        recieveCopy()
        check(server_files)



UDPSock.close()
os._exit(0)
