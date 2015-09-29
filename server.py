import sys
import socket

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock2= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Bind the socket to the port
server_address = ('localhost', 10000)
server_address2 = ('localhost', 6000)
print >>sys.stderr, 'starting up on %s port %s' % server_address

print >>sys.stderr, 'starting up on %s port %s' % server_address2
sock.bind(server_address)
sock2.bind(server_address2)

# Listen for incoming connections
sock.listen(1)
sock2.listen(1)

print >>sys.stderr, 'waiting for a connection'
connection, client_address = sock.accept()
connection2, client_address2 = sock2.accept()
print >>sys.stderr, 'connection from', client_address
print >>sys.stderr, 'connection from', client_address2

while True:
# Wait for a connection
# Receive the data in small chunks and retransmit it
#while True:
    #print >>sys.stderr, 'received "%s"' % data
#if data:
    #print >>sys.stderr, 'sending data back to the client'
    #connection2.sendall(data)
    data = connection.recv(512)
    if not data :
    	print >> sys.stderr, 'disconnect from client'
    break    
    else :
    	print >>sys.stderr, 'received "%s"' % data
    	print >>sys.stderr, 'sending data to clients'
    	connection2.sendall(data)
#else:
#print >>sys.stderr, 'no more data from', client_address
#break
    #print >>sys.stderr, 'received "%s"' % data2
#if data:
    #print >>sys.stderr, 'sending data back to the client'
    #connection.sendall(data2)
    data2 = connection2.recv(512)
    if not data2 :
    	print >> sys.stderr, 'disconnect from clients'
    break
    else :
    	print >>sys.stderr, 'received "%s"' % data2
    	print >>sys.stderr, 'sending data to client'
    	connection.sendall(data2)    
    	connection.close()            #else:
                 #   print >>sys.stderr, 'no more data from', client_address
                  #  break
        # Clean up the connection
	#connection.close()
