import rsa 
import pickle
import socket
import signalGenerator
from cryptography.fernet import Fernet
import Crypto
 
HOST = '127.0.0.1'
PORT = 62542
	
def get_private_key():
	fi = open('slave_private.txt','rb')
	key = pickle.load(fi)
	fi.close()
	return key
		
def listen():
	with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
		f = open('port.txt')
		PORT = int(f.read())
		f.close()
		s.connect((HOST,PORT))
		payload = ''
		while True:
			ID = s.recv(1024)
			if ID and ID.decode() == '6547':
				msg = "ID Authenticated"
				print(msg)
				s.sendall(msg.encode())
				sign = s.recv(48)
				payload = s.recv(1024)
				print("Received Payload: ",end='')
				print(payload,end='\n\n')
				if signalGenerator.verify_sig(sign,payload):
					print("Signature Verified !!")
					payload = Crypto.decrypt_payload_asymm(payload,get_private_key())
					count = payload[0] - 48
					key = payload[1:]
					print("Count bit Received : %d"%count)
					#print("Next Count Expected: %d"%count^1)
					print('Received Secret Key: ',end='')
					print(key,end='\n\n')
					msg = "ECU Unlocked!"
					s.sendall(Crypto.encrypt_payload_symm(msg,key))
					#else :
				#	print("ID not matched")
			else:
				msg = "Unable to Authenticate ID"
				s.sendall(msg.encode())	
				break
				
if __name__=='__main__':
	listen()
