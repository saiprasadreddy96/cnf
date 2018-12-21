import socket
def main():
	host = '10.1.135.30'
	port = 8000
	s = socket.socket()
	s.connect((host, port))
	
	while True:
		data = input("Type message to be sent to server")
		if data == 'q':
			break
		s.send(data.encode())
		data = s.recv(1024).decode()
		print("Received message is	" +str(data))
	s.close()

if __name__ == '__main__':
	main()