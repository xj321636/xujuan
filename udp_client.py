import socket
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
print('I am connecting the server!')
for data in ['aBch','h7Tq','.']:
	s.sendto(data.encode('utf-8'),('127.0.0.1',8088))
	str1=s.recv(1024).decode('utf-8')
	print('The original string is:',data,'\tthe processed string is:',str1)
s.close()
