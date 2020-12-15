import socket

# we can declare a server to run on this socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# bind our server to parameters
server.bind( ('localhost', 9874) ) # we provide a tuple of binding params
server.listen(5) # max requests
print('Server is running on localhost:9874')

# handle requests as they occur
while True:
    # get hold of the client and the address
    (client, addr) = server.accept() # accept returns values for client and their address
    # we can read as much as we like from the request - lets read up to 1024 bytes
    buf = client.recv(1024)
    print(f'server has received {buf}')
    # we may choose to respond to the requst
    client.send( buf.upper() ) # in this case we return the same data in upper case
    client.close()
    # if the user requested 'quit' then kill the server
    if buf == b'quit':
        print('server is closing')
        server.close()
        break
