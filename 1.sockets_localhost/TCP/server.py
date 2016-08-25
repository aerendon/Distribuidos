#!/usr/bin/env python

import socket
import math


TCP_IP = '127.0.0.1'
TCP_PORT = 5003

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((TCP_IP, TCP_PORT))
s.listen(1)

conn, addr = s.accept()
print 'Connection address:', addr
result = ""
while 1:
    data = conn.recv(1024)
    if not data: 
      break
    data = data.split(",")
    op = data[0]
    num1 = data[1]
    num2 = data[2]
    if(op == '+' or op == '-' or op == '*' or op == '/'):
      result = eval(num1 + op + num2)
    elif(op == '^'):
      result = eval("math.pow" + "(" + num1 + "," + num2 + ")")
    elif(op == "sqrt"):
      num2 = eval("1.0/" + num2)
      result = eval("math.pow" + "(" + num1 + "," + str(num2) + ")")
    elif(op == "log"):
      result = eval("math." + op + "(" + num1+", "+ num2 +")")
    elif(op == '0'):
      print "Solicitud de cerrar servidor aceptada"
      result = "Servidor apagado"
      conn.send(str(result))
      conn.close()
      break
    print "received data:", data
    conn.send(str(result))
