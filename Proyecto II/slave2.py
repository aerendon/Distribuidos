from socket import *
import os
import clock
import glob

host = "127.0.0.1"  # set to IP address of target computer
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


if __name__ == '__main__':
    #time_slave = clock.toTime(berckeley())
    #print time_slave
    # slaveFiles = files()
    server_files = contentFiles(files())
    print server_files
    filesCopy()
    recieveCopy()




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
