# Import socket module 
import socket			 

# Create a socket object 
s = socket.socket()		 

# Define the port on which you want to connect 
port = 9500				
msg = input("Please enter a message to the server")

# connect to the server on local computer 
s.connect(('127.0.0.1', port)) 

# send message to the server for input
s.sendmsg(msg)

# receive data from the server 
print(s.recv(1024) )
# close the connection 
s.close()	 
