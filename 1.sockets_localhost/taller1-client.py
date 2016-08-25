import os
from socket import *
host = "127.0.0.1" # set to IP address of target computer
port = 13000
buf = 1024
addr = (host, port)
UDPSock = socket(AF_INET, SOCK_DGRAM)
print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Potenciacion")
print ("6. Radicacion")
print ("7. Logaritmacion")
while True:
    data = raw_input("Ingrese la opcion deseada o 'exit' para salir:")
    UDPSock.sendto(data, addr)
    if data == "exit":
        break
    else:
        if int(data) < 1 or int(data) > 7:
            print ("Opcion no valida")
        else:
            a = raw_input("A : ")
            UDPSock.sendto(a, addr)
            b = raw_input("B : ")
            UDPSock.sendto(b, addr)

    (res, addr) = UDPSock.recvfrom(buf)
    print ("resultado :  " + res)
UDPSock.close()
os._exit(0)
