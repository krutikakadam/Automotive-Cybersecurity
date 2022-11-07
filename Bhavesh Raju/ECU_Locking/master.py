import socket
from cryptography.fernet import Fernet
import string
import random
id=input('Enter slave id: ')
slave_id= int(id)
def server_program():
    # get the hostname
    host = socket.gethostname()
    port = slave_id  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
    # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

    # configure how many client the server can listen simultaneously
    server_socket.listen(2)
    conn, address = server_socket.accept()  # accept new connection
    print("Connection from: " + str(address))
    i=0
    while True:
        
        # receive data stream. it won't accept data packet greater than 1024 bytes
        data = conn.recv(1024).decode()
        if not data:
            # if data is not received break
            break
        print("from connected user: " + str(data))
        key = Fernet.generate_key()
        key1=key.decode()
        password="hEuziQP32kugta0xDIy3JaF64UYqjvG8W20n60vBVdM="
        enpass=password.encode()
        fernet = Fernet(enpass)
        enkey= fernet.encrypt(key1.encode())
        enkey1=enkey.decode()
        if i==0 or i%2==0:
          conn.send(enkey1.encode())  # send data to the client
          
        else:
          N = 4
          res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))
          res1 = ''.join(format(ord(i), '04b') for i in res)
          conn.send(res1.encode())
        i+=1

    conn.close()  # close the connection


if __name__ == '__main__':
    server_program()
