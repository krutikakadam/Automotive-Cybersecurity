import socket
from cryptography.fernet import Fernet

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000  # socket server port number

    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server

    message = "Checking authentication"  # take input
    i=0
    j=0
    k=0
    while message.lower().strip() != 'bye':
        
        client_socket.send(message.encode())  # send message
        if i==0 or i%2==0:
          data = client_socket.recv(1024).decode()  # receive response
          data1= data.encode()
          password="hEuziQP32kugta0xDIy3JaF64UYqjvG8W20n60vBVdM="
          enpass=password.encode()
          fernet = Fernet(enpass)
          dekey = fernet.decrypt(data1).decode()

          print('Random key: ' + dekey)  # show in terminal
          m=2
        elif i%2==1 and m%2==0:
          data = client_socket.recv(1024).decode()
          print('Received from Master ECU: ' + data)
          m=0
        if j==0:
          message = "Authentication success"  # again take input
          j+=1
        if k==21:
          message = "bye"
        k+=1
        i+=1
        
    client_socket.close()  # close the connection


if __name__ == '__main__':
    client_program()
