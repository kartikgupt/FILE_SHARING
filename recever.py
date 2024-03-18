import socket
import os
import time

s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
host = input("host name :")

# try to connet
try:
    s.connect((host,22222))
    print("connected sucessfully")
except:
    print("unable to connect")
    exit(0)
#receiving the file
file_name = s.recv(100).decode()
file_size = s.recv(100).decode()
#open and write the file
with open("./rec/"+file_name,"wb") as file:
    c = 0
    start_time = time.time()
    while c<=int(file_size):
        data = s.recv(1024)
        if not (data):
            break
        file.write(data)
        c+=len(data)
     end_time = time.time()
print("totaltim taken ", end_time-start_time)

s.close()
