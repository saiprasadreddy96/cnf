import socket
def main():
	host = '10.1.135.30'
	port = 8000
	s = socket.socket()
	s.bind((host, port))
	s.listen(1)
	con, address = s.accept()
	print("Address is" +str(address))
	while True:
		data = con.recv(1024).decode()
		if not data:
			break;
		print("Message received is	" + str(data))
		data = str(data).upper()
		print("Sending Message	" + str(data))
		con.send(data.encode())
	con.close()

if __name__ == '__main__':
	main()
	
