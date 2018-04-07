import socket
import sys
import time

# CRIA SOQUETE 21
s21 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s21.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR , 1)
#s.bind(('wlan0', 0x0800))

# ESCOLHE SERVER
#alvo = socket.gethostbyname("ftp.dca.fee.unicamp.br")
alvo = socket.gethostbyname("ftp.ed.ac.uk")
#alvo = socket.gethostbyname("ftp.inf.puc-rio.br")

# CONECTA AO SERVER
s21.connect((alvo, 21))
time.sleep(3)

# ENVIA USERNAME
buff = s21.recv(4028)
print buff
if '220' in buff:
	s21.sendall("USER anonymous\r\n")
	print "USERNAME SENT\n"
buff = s21.recv(1024)
print buff

# ENVIA PASSWORD
time.sleep(3)
if '331' in buff:
	s21.sendall("PASS edison@ecomp.poli.br\r\n")
	print "PASSWORD SENT\n"
buff = s21.recv(1024)
print buff

# ENVIA PASV
time.sleep(3)
if '230' in buff:
	s21.sendall("PASV\r\n")
	print "PASV SENT\n"

# RECEBE IP E PORT DO SERVER
buff0 = s21.recv(65000)
# 227 Entering Passive Mode (143,106,148,79,102,8). and more...
print(buff0)

si = buff0.find('227')
sf = buff.find(').')
buff = buff0[si:sf + 2]
print buff

buff = buff.split()
# ['227', 'Entering', 'Passive', 'Mode', '(143,106,148,79,102,8).']
buff = buff[4]
print buff
# '(143,106,148,79,102,8).'
buff = buff.split(',')
print buff
# ['(143', '106', '148', '79', '102', '8).']
p1 = buff[4]
print p1
# '102'
#print buff0[5]
# '8).'
p2 = buff[5].split(').')[0]
print p2
port = 256 * int(p1) + int(p2)
print port
# '8'

if '227' in buff0:
    s21.sendall("LIST\r\n")
    print "LIST SENT "

s20 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s20.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s20.connect((alvo, port))

data = s20.recv(1024)
print "DATA:\n", data

time.sleep(10)

s20.sendall("QUIT\r\n")
buff = s21.recv(1024)
print "QUIT20: ", buff

s21.sendall("QUIT\r\n")
buff = s21.recv(1024)
print "QUIT21: ", buff

s20.close()


time.sleep(10)

s21.sendall("QUIT\r\n")
buff = s21.recv(1024)
print "QUIT21: ", buff

s21.close()
