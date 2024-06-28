# Client-Server System Using TCP Sockets

## Overview
This project involves designing and implementing a Client-Server system that uses TCP sockets to enable communication between a client and a server. The client initiates communication, sends arithmetic operation requests, and receives computed results from the server.

![Client-Server System](Arithmetic ChatBot/image.png)

## Functionality

### Client
1. **Initiates Communication**: The client starts by sending its name to the server. This name is remembered by the server for the entire communication session.
2. **User Input**: The client runs in an infinite loop where it accepts a line of input from the user. The input is expected to be a string consisting of two numbers and a simple arithmetic operation (e.g., "12 + 42", "3.24 - 45", or "4.5 / -6").
3. **Input Validation**: If the input is not correctly formatted, a warning is displayed to the user. If the input is valid, the client sends this string to the server.
4. **Receive and Display Result**: The client receives the computed result from the server and displays it.
5. **End Session**: If the user inputs 'q', the client sends this signal to the server to end the session, terminates the connection, and prints "Session ended".

### Server
1. **Set Up Server**: The server creates a TCP socket, binds it to a specific host and port, and listens for incoming connections.
2. **Accept Connection**: Upon accepting a connection from the client, the server receives and prints the client's name.
3. **Process Requests**: The server runs an infinite loop to continuously receive requests from the client. For each request, it parses the received arithmetic operation, computes the result, sends it back to the client, and prints the operation and result.
4. **End Session**: If the received message from the client is 'q', the server terminates the connection, prints "Session ended", and closes the connection socket.

## Code Description
### Server Program
- **Socket Creation**: The server creates a TCP socket using `socket.socket()` with `AF_INET` address family and `SOCK_STREAM` socket type.
- **Binding**: It binds the socket to a specific host and port using `bind()`.
- **Listening**: The server listens for incoming connections using `listen()` with a specified maximum number of queued up clients.
- **Accept Connection**: Upon accepting a connection using `accept()`, it receives the client's name and prints it.
- **Infinite Loop**: The server enters an infinite loop to continuously receive requests from the client.
  - **Parse and Compute**: For each request, it parses the received arithmetic operation, computes the result, sends it back to the client, and prints the operation and result.
  - **End Session**: If the received message from the client is 'q', the server terminates the connection and prints "Session ended".
- **Close Connection**: Finally, it closes the connection socket.

### Client Program
- **Socket Creation**: The client program creates a TCP socket similar to the server.
- **Connecting**: It connects to the server using `connect()` with the server's hostname and port.
- **Send Name**: It sends its name to the server.
- **Infinite Loop**: The client enters an infinite loop to continuously prompt the user to input arithmetic operations.
  - **Send Operation**: For each valid input, it sends the operation string to the server.
  - **Receive Result**: It receives the result from the server and prints it.
  - **End Session**: If the user inputs 'q', the client sends this signal to the server and terminates.
- **Close Socket**: It closes the socket after the session ends.

## Conclusion
This project demonstrates the implementation of a basic Client-Server system using TCP sockets in Python, where the client and server can communicate, process arithmetic operations, and handle session termination gracefully.
