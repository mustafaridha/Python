import socket
import sys
import os
import time
from time import sleep
while True:
    s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    os.system('Date/t >> Z:/Mustafa/Ping/pinglog.txt')
    os.system('Time/t >> Z:/Mustafa/Ping/pinglog.txt')
    rep = os.system('ping ' + '192.168.16.20 >> Z:/Mustafa/Ping/pinglog.txt')
    for i in range(60,0,-1):
        sys.stdout.write(str(i)+' ')
        sys.stdout.flush()
        sleep(1)
    print("\n")
