# first of all import the socket library 
import socket			 

# next create a socket object 
s = socket.socket()		 
print("Socket successfully created")

# reserver socket 9500 
port = 9500				

#bind to the port
s.bind(('', port))		 
print("socket binded to %s" %(port) )

# put the socket into listening mode 
s.listen(5)	 
print("socket is listening")

#while loop for communication with the client
while True: 

    # Establish connection with client. 
    c, addr = s.accept()	 
    print('Got connection from', addr )

    # send a thank you message to the client. 
    c.send('Thank you for connecting') 

    if s.recvmsg == "Hello" :
        s.sendmsg('Hi')
    else:
        s.sendmsg('Goodbye')

    # Close the connection with the client 
    c.close() 
