#!/usr/bin/env python
# -*- coding: utf-8 -*-

import socket
import sys
import time

# ETAPA DE OBTENCAO DO ENDERECO IP ATUAL
aux = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
aux.connect(("8.8.8.8",53))
meuIP = aux.getsockname()[0]
print "meuIP: ", meuIP, '\n'
meuIPort = aux.getsockname()[0].replace(".", ",")
aux.close()

#alvo = socket.gethostbyname("ftp.dca.fee.unicamp.br")
#alvo = socket.gethostbyname("ftp.ed.ac.uk")
alvo = socket.gethostbyname("ftp.inf.puc-rio.br")

# CRIA SOQUETE 21
s21 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket criado"
print s21.getsockname()
s21.connect((alvo, 21))
print "Server 21 conectado"

ClientPort = meuIPort + "," + str(8) + "," + str(1) #????????????
print "PORT: ", ClientPort

'''
# CRIA SOQUETE 20
#def skt20(seelf):
s20 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket criado"
s20.bind(('', 2049))
print s20.getsockname()
s20.connect((alvo, 20))
print "Server 20 conectado"

print "\nUSING ACTIVE MODE!\n"
'''
buff = s21.recv(1024)
print buff
if '220' in buff:
	s21.sendall("USER anonymous\r\n")
	print "USERNAME SENT\n"

buff = s21.recv(1024)
print buff
if '331' in buff:
	s21.sendall("PASS edison.qa@gmail.com\r\n")
	print "PASSWORD SENT\n"

buff = s21.recv(1024)
print buff

time.sleep(10)
if '230' in buff:
	s21.sendall("PORT " + ClientPort + "\r\n")
	print "PORT SENT\n"

buff = s21.recv(1024)
print buff

time.sleep(10)
if '200' in buff:
    s21.sendall("LIST\r\n")
    print "LIST SENT\n"

# CRIA SOQUETE 20
#def skt20(seelf):
s20 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print "Socket criado"
s20.bind(('', 2049))
print s20.getsockname()
s20.connect((alvo, 20))
print "Server 20 conectado"

# SERVER ENVIA UM 150 INDICANDO QUE 
# ESTA ABRINDO A CONEXÃO DE DADOS (ASCII MODE)
# PARA LIST (/bin/ls)
#time.sleep(10)
buff = s20.recv(1024)
print buff
'''
#if ' ' in buff:
s20 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print '71'
s20.bind(("localhost", 2049))
print '73'
s20.listen(2)
print "75"
conn, addr = s20.accept()
print '\nConnection up no socket:', conn
print '\nEndereco do cliente (IP, porta): ', addr
data = s20.recv(4096)
print data
s20.close()
'''

#buff = s21.recv(1024)
#print buff

#if '226' in buff:
s21.sendall("QUIT\r\n")
print "QUIT21"
#s20.sendall("QUIT\r\n")
#print "QUIT20"

#s20.close()
s21.close()
#conn.close()

