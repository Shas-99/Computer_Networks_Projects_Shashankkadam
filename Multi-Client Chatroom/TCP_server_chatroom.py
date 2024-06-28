# This is the Server program
#
# Sequence of steps:
# 1. create a "welcome" socket for listening to new connections
# 2. bind the socket to a host and port
# 3. start listening on this socket for new connections
# 4. accept an incoming connection from the client
#   5. send and receive data over the "connection" socket


import socket
import threading
from datetime import datetime


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


clients = []
names = []
timeout = 15
s.settimeout(timeout)

def broadcast(clients,msg,from1):
	for i in clients:
		if i==from1:
			continue
		else:
			i.send(msg.encode('utf-8'))
		
def handle(connection_socket,clients):
	ind = 0
	while(True):
		resp = connection_socket.recv(1024)
		if resp.decode() == "q":
			ind= clients.index(connection_socket)
			n = names[ind]
			msg = f'{n}: Bye guys.. See ya later...'
			broadcast(clients,msg,connection_socket)
			msg = f'ONE OF OUR MEMBER {n} HAS LEFT THE CHATROOM'
			print(msg)
			broadcast(clients,msg,connection_socket)
			connection_socket.close()
			clients.remove(connection_socket)
			names.remove(n)
			break
			
		else:
			print(resp.decode())
			broadcast(clients,resp.decode(),connection_socket)
	
		
#  create a socket for listening to new connections

# use SOCK_STREAM for TCP
# use SOCK_DGRAM for UDP

# bind it to a host and a port
host = '10.250.9.121'
port = 22223# arbitrarily chosen non-privileged port number
s.bind((host,port))
print("SERVER STARTED.. WAITING FOR CONNECTION FROM CLIENTS..")

s.listen()

# accept a connection

try:
	while True:
		try:
			connection_socket, addr = s.accept()
			msg = connection_socket.recv(1024)
			current_datetime = datetime.now()
			h = current_datetime.hour
			m = current_datetime.minute
			s2 = current_datetime.second
			clients.append(connection_socket)
			names.append(msg.decode())
			rep = f'SERVER : {msg.decode()} HAS LOGGED IN TO THE SERVER AT {h}:{m}:{s2}.MEMBER COUNT = {len(clients)}'
			print(rep)
			broadcast(clients,rep,connection_socket)
			connection_socket.send('YOU ARE NOW CONNECTED. FEEL FREE TO CHAT AS OUR CHATROOM IS SECURE'.encode('utf-8'))
			thread = threading.Thread(target=handle, args=(connection_socket,clients,))
			thread.start()
		
		except socket.timeout:
			if(len(clients)==0):
				print("NO MORE REQUESTS\nCLOSING THE CHATBOT SERVER")
				break
			else:
				continue
finally:
	s.close()
