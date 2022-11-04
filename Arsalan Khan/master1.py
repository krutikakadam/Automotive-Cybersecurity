import signalGenerator
import rsa 
import pickle
import socket
import Crypto
import change_port
from cryptography.fernet import Fernet
ID = ""
HOST = '127.0.0.1'
PORT = 62542
def get_ID():
	global ID
	ID = input("Enter ID: ")

def get_count():
	fi = open('counter.txt')
	count = int(fi.read())
	count ^=1
	fi.close()
	fi = open('counter.txt','w')
	fi.write(str(count))
	return str(count)
	
def get_public_key():
	fi = open('slave_public.txt','rb')
	public = pickle.load(fi)
	fi.close()
	return public		
	
def gen_secret_key():
	key = Fernet.generate_key()
	print("Secret key : ",end='')
	print(key,end='\n\n')
	return key

def establish_connection():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: 
		PORT = change_port.get_port()
		s.bind((HOST, PORT))
		s.listen()
		print("Establishing Connection...")
		conn, addr = s.accept()
		with conn:
			get_ID()
			for i in range(1):
				conn.sendall(ID.encode())
				recv = conn.recv(1024)
				if recv.decode() != 'ID Authenticated':
					print("ID Authentication Failed !")
					break
				key = gen_secret_key()
				payload = key
				count = get_count().encode()
				#count = 1
				#print("Count bit set")
				payload = count + payload
				payload = Crypto.encrypt_payload_asymm(payload,get_public_key())
				sign = signalGenerator.generate_signature(payload)
				conn.sendall(sign)
				conn.sendall(payload)
				print('Payload sent',end='\n\n')
				while True:
					recv = conn.recv(1024)
					if not recv:
						print("Break")
						break
					else:
						print(Crypto.decrypt_payload_symm(recv,key).decode())
						
				#else:
				##	break
if __name__=='__main__':
	#generate_master_pki()
	#get_ID()
	establish_connection()
	
	
