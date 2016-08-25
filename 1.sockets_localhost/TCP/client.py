#!/usr/bin/env python

import socket


TCP_IP = '127.0.0.1'
TCP_PORT = 5003
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
while(1):
  print ""
  print "-------------------MENU-----------------------"
  print "SUMA: '+'"
  print "RESTA: '-'"
  print "MULTIPLICACION: '*'"
  print "DIVISION: '/'"
  print "POTENCIACION: '^'"
  print "RADICACION: 'sqrt'"
  print "LOGARITMACION: 'log'"
  print "SALIR: '0'"
  
  BOOL_VALID_OP = True
  op = raw_input("Que operacion desea realizar: ")
  message = ""
  if(op == '+' or op == '-' or op == '*'):
    num1 = raw_input("Ingrese el numero 1: ")
    num2 = raw_input("Ingrese el numero 2: ")
  elif(op == '/'):
    num1 = raw_input("Ingrese el numero 1: ")
    num2 = raw_input("Ingrese el numero 2: ")
    while(num2 == '0'):
      num2 = raw_input("El divisor debe ser diferente de 0. Ingreselo nuevamente: ")
  elif(op == '^'):
    num1 = raw_input("Ingrese base: ")
    num2 = raw_input("Ingrese exponente: ")
  elif(op == "sqrt"):
    num1 = raw_input("Ingrese base: ")
    num2 = raw_input("Ingrese indice: ")
  elif(op == "log"):
    num1 = raw_input("Ingrese base: ")
    num2 = raw_input("Ingrese numero: ")
  elif(op == '0'):
    num1 = 0
    num2 = 0
    message = op + "," + str(num1) + "," + str(num2)
    s.send(message)
    result = s.recv(1024)
    print result
    s.close()
    break
  else:
    print "Operacion no valida"
    BOOL_VALID_OP = False

  if(BOOL_VALID_OP):
    message = op + "," + str(num1) + "," + str(num2)
    s.send(message)
    result = s.recv(1024)
    print "El resultado es: ", result

