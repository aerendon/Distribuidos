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
            (res, addr) = UDPSock.recvfrom(buf)
            res = res.split(",")
#            addr1 = (hots, res[0])
#            addr2 = (hots, res[1])
#            addr3 = (hots, res[2])
            a = raw_input("A : ")
            b = raw_input("B : ")
            for i in range(3):
                res[i] = int(res[i])
                UDPSock.sendto(data, (host, res[i]))
                UDPSock.sendto(a, (host, res[i]))
                UDPSock.sendto(b, (host, res[i]))
                (resop, (hots, res[i])) = UDPSock.recvfrom(buf)
                print ("resultado del intengrante " + str(i) +" : " + resop)
UDPSock.close()
os._exit(0)
