import socket, sys

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect( ('localhost', 9874) )

# check to see if ther were any runtime arguments passed to this client
if len(sys.argv) > 1:
    message = ' '.join(sys.argv[1:])
else:
    message = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam luctus et erat et pretium. Nam vitae lectus pharetra, dignissim risus nec, pellentesque orci. Nunc ac est in orci sodales vestibulum id id purus. Pellentesque scelerisque odio a mollis mattis. Morbi feugiat arcu a consequat dictum. Integer varius ante nec est mattis faucibus. Quisque eu orci a justo mollis ultricies in ac dolor. Nunc lobortis tortor ante.
Morbi risus lorem, tristique ut volutpat eget, dictum sit amet sapien. In a ultricies lectus, in viverra nisi. Fusce turpis urna, lacinia eget arcu a, porta efficitur eros. Cras ac mauris eget risus ullamcorper commodo quis ac dui. Cras non lectus vestibulum, porta felis nec, vestibulum eros. Nam dapibus eleifend lorem et pretium. Mauris id ex in nulla laoreet lacinia tempus eu metus. In hac habitasse platea dictumst. Sed lorem sem, cursus et neque at, cursus dapibus lorem. Nam nec diam eu odio imperdiet convallis ac nec ligula. In mattis malesuada enim nec tristique. Donec a aliquam ipsum. Duis feugiat at velit id tincidunt. Maecenas sagittis, diam quis consectetur luctus, arcu lorem porta mauris, sit amet interdum neque risus id ipsum.
Nunc ut nisi urna. Aliquam malesuada blandit augue vel cursus. Suspendisse dignissim nisl et purus sagittis vulputate. Quisque vel sapien nec risus semper tincidunt non in velit. Quisque a mollis mauris. Maecenas et elit enim. Vivamus luctus, risus ac vulputate placerat, nibh lorem tincidunt ex, et accumsan ligula nibh ut augue. Aenean in felis ut massa elementum pretium. Phasellus porta pretium velit eget fermentum. Duis blandit ac elit varius rhoncus. Fusce ante enim, placerat a gravida non, semper sit amet tortor.
Vestibulum accumsan tortor et augue maximus vehicula. Nulla risus eros, venenatis at tortor eu, hendrerit eleifend quam. Fusce nec blandit sapien. Mauris diam enim, molestie ut tempor non, mattis et quam. Nam feugiat neque erat, in viverra turpis tincidunt at. Etiam ut arcu porta urna volutpat varius. Etiam condimentum nunc est, sit amet interdum laoreet.
'''

# now we can send our message to the server
sock.send(message.encode()) # we make sure it is encoded for http transfer
# if there is a response handle it here
data = sock.recv(4096) # plenty
# convert from byte to string then print
str_data = data.decode()
print(str_data)
sock.close() # tidy up