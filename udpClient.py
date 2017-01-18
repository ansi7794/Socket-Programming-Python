import socket

def Main():
	host = '127.0.0.1'
	port = 3001

	srvr = ('127.0.0.1' , 3000)

	soc = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
	soc.bind((host,port))

	data = raw_input("enter message - ")

	while data != "quit":
		soc.sendto(data,srvr)
		rec_data , rec_addrs = soc.recvfrom(2048)
		print "data received from server - " + str(rec_data)
		data = raw_input("enter message - ")
	soc.close()

if __name__ == '__main__':
	Main()