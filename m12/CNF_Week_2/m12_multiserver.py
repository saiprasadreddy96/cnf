import socket
import threading
from _thread import *
import csv

def Main():
    loc = ("F://recyle bin//MSIT//cnf//m12//CNF_Week_2//data.csv")
    rows = []
    with open(loc, 'r') as csvfile: 
    # creating a csv reader object 
        csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
        #fields = csvreader.next() 
  
    # extracting each data row one by one 
        for row in csvreader: 
            rows.append(row) 
  
    # get total number of rows 
    #     print("Total no. of rows: %d"%(csvreader.line_num))
    # for row in rows[:10]: 
    # # parsing each column of a row 
    #     for col in row: 
    #         print(col), 
    #     print('\n') 

    # for row in rows:
    #     print(row)


    host = '10.10.8.248'
    port = 5001
    clients = []
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(20)
    while True:
        c, addr = s.accept()
        print("Connected Server" +str(addr))
        
        start_new_thread(clientsThread,(c, rows))
def clientsThread(c, rows):

    while True:
        data = c.recv(1024)
        if not data:
            break
        if data.decode() == 'Q':
            break
        value = int(data.decode())
        flag = 0
        for row in rows:
            if int(row[0]) == value:
                flag = 1
                q = row[1]
                a = row[2]
        if flag == 0:
            str1 = "ROLLNUMBER-NOTFOUND"
            c.send(str1.encode())
        else:
            str1 = "ROLLNUMBER-FOUND"
            #print("sending question")
            c.send(str1.encode())
            while True:
                print("sending question")

                c.send(q.encode())
                ca = c.recv(1024).decode()
                if a == (ca):
                    str1 = "ATTENDANCE SUCCESS"
                    c.send(str1.encode())
                    break;
                else:
                    str1 = "ATTENDANCE FAILURE"
                    c.send(str1.encode())



    
    c.close()
if __name__ == '__main__':
    Main()