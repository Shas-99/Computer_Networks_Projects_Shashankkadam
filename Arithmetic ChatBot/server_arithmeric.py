# This is the Server program that uses UDP
#
# Sequence of steps:
#   1. create a socket  
#   2. bind the socket to a host and port address
#   3. start sending and receiving data on this socket


import socket
from datetime import datetime
import time,random
 
#  create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
timeout = 5
s.settimeout(timeout)

    # The first argument should be AF_INET
        # The second argument is SOCK_STREAM for TCP service
            #    and SOCK_DGRAM for UDP service

            # bind it to a host and a port
host = '10.250.9.166'
port = 22225

  # arbitrarily chosen non-privileged port number
s.bind((host,port))

print("SERVER STARTED..WAITING FOR CONNECTION FROM CLIENT....")
data, addr = s.recvfrom(1024)
print("\nSERVER RECEIVED REQUEST:", data.decode())
if(data.decode() == "SEND_DATE"):
	current_datetime = datetime.now()	
	year = current_datetime.year
	month = current_datetime.month
	date = current_datetime.day
	data = f"\nRESPONSE TO THE REQUEST : {date}-{month}-{year}"
#formatted_datetime = current_datetime.strftime("%Y-%m-%d")
	s.sendto(data.encode('utf-8'), addr)
	print(data)
elif(data.decode() == "SEND_TIME"):
	current_datetime = datetime.now()
	hour = current_datetime.hour
	m = current_datetime.minute
	s2 = current_datetime.second
	data = f"\nRESPONSE TO THE REQUEST : {hour}::{m}::{s2}"
#formatted_datetime = current_datetime.strftime("%Y-%m-%d")
s.sendto(data.encode('utf-8'), addr)
print(data)

    # receive some bytes and print them
try:
while(True):
data, addr = s.recvfrom(1024)
print("\nSERVER RECEIVED REQUEST:", data.decode())
if(data.decode() == "SEND_DATE"):
current_datetime = datetime.now()
year = current_datetime.year
month = current_datetime.month
date = current_datetime.day
data = f"\nRESPONSE TO THE REQUEST : {date}-{month}-{year}"
#formatted_datetime = current_datetime.strftime("%Y-%m-%d")
s.sendto(data.encode('utf-8'), addr)
print(data)
elif(data.decode() == "SEND_TIME"):
current_datetime = datetime.now()
hour = current_datetime.hour
m = current_datetime.minute
s2 = current_datetime.second
data = f"\nRESPONSE TO THE REQUEST : {hour}::{m}::{s2}"
#formatted_datetime = current_datetime.strftime("%Y-%m-%d")
s.sendto(data.encode('utf-8'), addr)
print(data)
except socket.timeout:
print("\nNO REQUEST RECIEVED.. SERVER TERMINATED.")

finally:
s.close()# This is the Server program that uses UDP