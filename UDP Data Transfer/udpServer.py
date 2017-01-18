import socket

def Main():
	host = '127.0.0.1'
	port = 3000

	soc = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	soc.bind((host,port))

	print "Server Initiated"
	while True:
		data,addrs = soc.recvfrom(2048)
		print "The data from - " + str(addrs) + " is - " + str(data)
		data = str(data).lower()
		print "data to be sent - " + str(data)
		soc.sendto(data,addrs)
	soc.close()


if __name__ == '__main__':
	Main()