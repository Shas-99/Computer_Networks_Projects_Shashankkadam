import threading
import socket

# Get the user's login name
name = input('Enter your Login Name: ')

# Create a socket object and connect to the server
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('10.250.9.121', 22223))
client.send(name.encode('utf-8'))

# Function to receive messages from the server
def client_receive():
    while True:
        message = client.recv(1024).decode('utf-8')
        print(f"{message}")

# Start a thread to handle incoming messages
receive_thread = threading.Thread(target=client_receive, daemon=True)
receive_thread.start()

# Main loop to send messages to the server
while True:
    message = f'{name}: {input("")}'
    if message == f'{name}: q':
        client.send("q".encode('utf-8'))
        break
    else:
        client.send(message.encode('utf-8'))

# Close the connection
client.close()
