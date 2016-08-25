import os
from socket import *
host = "192.168.8.63" # set to IP address of target computer
port = 13001
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
while True:
    data = raw_input("Ingrese la vocal deseada o 'exit' para salir:")
    if data == "exit":
        break
    elif (str(data) == 'a' or str(data) == 'e' or str(data) == 'i' or str(data) == 'o' or str(data) == 'u'):
            UDPSock.sendto(data, addr)
            (res, addr) = UDPSock.recvfrom(buf)
            print ("La vocal esta : " + res + " veces")
    else:
             print "Opcion no valida"
UDPSock.close()
os._exit(0)
