import sys
import time
import os
from socket import *

host = "127.0.0.1" # set to IP address of target computer
port1 = 13000
buf = 1024
addr = (host, port1)
UDPSock = socket(AF_INET, SOCK_DGRAM)
time1 = time.strftime("%H:%M:%S")
print ("enviando")
UDPSock.sendto(time1, addr)
(time2, addr) = UDPSock.recvfrom(buf)
print ("mi hora : " + time1)
print ("hora del equipo 2 : " + time2)
hora1= time1[0:2] 
minutos1= time1[3:5]
segundos1= time1[6:8]
hora1=int(hora1)
minutos1=int(minutos1)
segundos1=int(segundos1)
horaSegundos1= segundos1 + (minutos1*60) + (hora1*3600)
hora2= time2[0:2] 
minutos2= time2[3:5]
segundos2= time2[6:8]
hora2=int(hora2)
minutos2=int(minutos2)
segundos2=int(segundos2)
horaSegundos2= segundos2 + (minutos2*60) + (hora2*3600)
promedio= (horaSegundos1+horaSegundos2)/2
if (promedio>=horaSegundos1):
    (listo, addr) = UDPSock.recvfrom(buf)
    horaSegundos1=int(listo)
else:
    timau = promedio
    while (timau<horaSegundos1):
        time.sleep(2)
        timau=timau + 2
        horaSegundos1=horaSegundos1 + 1

listo1=str(horaSegundos1)
UDPSock.sendto(listo1, addr)      
horafinal=promedio/3600
au= (horaSegundos1%3600)
minutosfinal=(au/60)
segundosfinal= (au%60)      

print ("hora actualizada "+str(horafinal)+":"+str(minutosfinal)+":"+str(segundosfinal))
UDPSock.close()
os._exit(0)