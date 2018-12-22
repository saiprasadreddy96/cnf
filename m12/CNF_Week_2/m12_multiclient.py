import socket
def Main():
    host = '10.10.8.248'
    port = 5001
    client = True
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.connect((host, port))


    print("Connected")
    
    message = input("Enter your roll number")
    while message != 'Q':

        s.send(message.encode())
        valid = s.recv(1024).decode()
        if str(valid) == 'ROLLNUMBER-NOTFOUND':
            print("ROLLNUMBER-NOTFOUND")
        else:
            print("ROLLNUMBER-FOUND")
            
            while True:
                q = str(s.recv(1024).decode())
                print("Question from server is" +q)
                print("Enter your answer")
                ca = input()
                s.send(ca.encode())
                valid = s.recv(1024)
                valid = str(valid.decode())
                if valid == "ATTENDANCE SUCCESS":
                    break;
                else:
                    str = "ATTENDANCE FAILURE"
                    #c.send(str.encode())

        
        message = input("-> ")
    s.close()
if __name__ == '__main__':
    Main()