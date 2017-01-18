import socket

def Main():
	host = '127.0.0.1'
	port = 3000

	soc = socket.socket()
	soc.bind((host,port))

	soc.listen(1)
	con , addr = soc.accept()
	print "Connection from - " + str(addr)
	while True:
		data = con.recv(2048)
		if not data:
			break
		print "from connected device - " + str(data)
		data = str(data).lower()
		print "data to be sent - " + str(data)
		con.send(data)
	con.close()


if __name__ == '__main__':
	Main()