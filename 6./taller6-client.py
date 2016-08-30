import os
import xmlrpclib

s = xmlrpclib.ServerProxy('http://localhost:8000')

print ("1. Suma")
print ("2. Resta")
print ("3. Multiplicacion")
print ("4. Division")
print ("5. Potenciacion")
print ("6. Radicacion")
print ("7. Logaritmacion")

while True:
    data = raw_input("Ingrese la opcion deseada o 'exit' para salir:")
    if data == "exit":
        break
    else:
        if int(data) < 1 or int(data) > 7:
            print ("Opcion no valida")
        else:
            a = raw_input("A : ")
            b = raw_input("B : ")
        if (data == "1"):
            res = s.suma(a, b)
        if (data == "2"):
            res = s.resta(a, b)
        if (data == "3"):
            res = s.multiplicacion(a, b)
        if (data == "4"):
            res = s.division(a, b)
        if (data == "5"):
            res = s.potenciacion(a, b)
        if (data == "6"):
            res = s.radicacion(a, b)
        if (data == "7"):
            res = s.logaritmo(a, b)

    print ("resultado :  " + str(res))
os._exit(0)
