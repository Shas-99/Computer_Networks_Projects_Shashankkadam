'''
Client Programme for Arithmetic Bot
 -- Created by Shashank Kadam (Github- Shas-99)
'''


# Sequence:
#
# 1. Create a socket
# 2. Connect it to the server process. 
#	We need to know the server's hostname and port.
# 3. Send and receive data 

import socket

# create a socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	# The first argument AF_INET specifies the addressing family (IP addresses)
	# The second argument is SOCK_STREAM for TCP service
	#    and SOCK_DGRAM for UDP service


# connect to the server
host='10.250.9.166'
port=22333  # this is the server's port number, which the client needs to know
s.connect((host,port))


# send some bytes
name = "Arithmetic Process"
s.send(name.encode('utf-8'))

while(True):
	string = input("\nEnter Arithmetic Operation with spaces between numbers and operator: ")
	if(string == "q"):
		s.send(string.encode('utf-8'))
		break
	else:
		t = string.split(' ')
		if(len(t)!=3):
			print("Incorrect String. Enter Again")
			continue
		else:
			k = t[1]
			if(k!='+' and k!='-' and k!='*' and k!='/'):
				print("Incorrect string. Enter again")
				continue
			else:
				s.send(string.encode('utf-8'))
		
		response = s.recv(1024)
		print("CLIENT RECEIVED: ",response.decode())
		
		
s.close()
# read a response


# close the connection