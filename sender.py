import socket
import os ,time
s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
s.bind((socket.gethostname(),22222))
s.listen(5)
print("host:", s.getsockname())

#accepting the connection from client
client , addr = s.accept()

#getting the file details
file_name = input("file name ")
file_size= os.path.getsize((file_name))

#send the file

client.send(file_name.encode())
client.send(str(file_size).encode())

#open and read file
with open(file_name,+'rb') as file:
    c=0
    start_time = time.time()
    while c<= file_size:
        data = file.read(1024)
        if not(data):
            break
        client.sendall(data)
        c+=len(data)

    end_time= time.time()
print("total time ", end_time-start_time)
s.close()