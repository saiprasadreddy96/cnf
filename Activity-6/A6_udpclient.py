import socket
def main():
	host = '10.1.135.30'
	port = 8001
	server = ('10.1.135.30', 8000)
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	while True:
		data = input("Type message to be sent: ")
		if data == 'q':
			break;
		s.sendto(data.encode(), server)
		data, address = s.recvfrom(1024)
		print("message received is :" +str(data))
	s.close()

if __name__ == '__main__':
	main() 
