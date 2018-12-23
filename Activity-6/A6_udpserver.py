import socket
def main():
	host = '10.1.135.30'
	port = 8000
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host, port))
	while True:
		data, address = s.recvfrom(1024)
		if not data:
			break;
		print("Received data is	" +str(data.decode()))
		data = str(data.decode()).upper()
		s.sendto(data.encode(), address)
		print("Sending data " +str(data))
	s.close()

if __name__ == '__main__':
	main()
