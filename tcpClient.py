import socket

def Main():
	host = '127.0.0.1'
	port = 3000

	soc = socket.socket()
	soc.connect((host,port))

	data = raw_input("enter message - ")

	while data != "quit":
		soc.send(data)
		rec_data = soc.recv(2048)
		print "data received from server - " + str(rec_data)
		data = raw_input("enter message - ")
	soc.close()

if __name__ == '__main__':
	Main()