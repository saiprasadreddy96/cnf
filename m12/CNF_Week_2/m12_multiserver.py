import socket
import threading
import random
import time
from threading import *
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
        
        start_new_thread(clientsThread,(c,x))
def clientsThread(c):

    while True:
        data = c.recv(1024)
        if not data:
            break
        if data.decode() == 'Q':
            return
        value = int(data.decode())
        flag = 0
        for row in rows:
            if row[0] == value:
                flag = 1
                q = row[1]
                a = row[2]
        if flag == 0:
            str = "ROLLNUMBER-NOTFOUND"
            c.send(str.encode())
        else:
            str = "ROLLNUMBER-FOUND"
            #print("sending question")
            c.send(str.encode())
            while True:
                print("sending question")

                c.send(q.encode())
                ca = c.recv(1024)
                if a == str(ca.decode()):
                    str = "ATTENDANCE SUCCESS"
                    c.send(str.encode())
                    break;
                else:
                    str = "ATTENDANCE FAILURE"
                    c.send(str.encode())



    
    c.close()
if __name__ == '__main__':
    Main()