import cryptography 
import freshnessmanager
import hmac
import hashlib
from cryptography.fernet import Fernet
#from collection import counter 
key_data=Fernet.generate_key()
#print("Key:",key_data)

Master_id=12267

file=open('key_value','wb')
file.write(key_data)
file.close()

Data="'Speed=100Kmph', 'Gear=5'"
encoded=Data.encode()
f=Fernet(key_data)
encrypted=f.encrypt(encoded)
print("Encrypted Data:",encrypted)
fv = freshnessmanager.getFV()
print('Freshness Value: %s'%fv)
freshnessmanager.incFV()

file=open('encrypted_data','wb')
file.write(encrypted)
file.close()

import pyAesCrypt,os
buffersize=256*1024
password=input("Enter your password: ")
pyAesCrypt.encryptFile("key_value","key_value.aes",password,buffersize)
os.remove("key_value")


def generateMAC(message,key,fv):
	payload= bytes(message,'utf-8') + key + bytes(fv,'utf-8')
	mac = hmac.new(key,payload, hashlib.sha1)
	return mac

def generateSPDU(message,fv,mac):
	SPDU = bytes(message,'utf-8') + bytes(fv,'utf-8') + mac.digest()
	return SPDU
	
def generateSKey():
	key=Fernet.generate_key()
	return key
	
if __name__=='__main__':
	message = 'Secure on board'
	#fv = freshnessmanager.getFV()
	#print('Freshness Value: %s'%fv)
	key = generateSKey()	
	mac = generateMAC(message,key,fv)
	SPDU = generateSPDU(message,fv,mac)
	#freshnessmanager.incFV()
	print(SPDU)



