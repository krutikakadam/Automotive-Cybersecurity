import FreshnessManager
import hmac
import hashlib
from cryptography.fernet import Fernet	

def generateMAC(msg,key,freshnessValue):
	payload= bytes(msg,'utf-8') + key + bytes(freshnessValue,'utf-8')
	mac = hmac.new(key,payload, hashlib.sha1)
	return mac

def generateSecurePDU(msg,freshnessValue,mac):

	SecurePDU = bytes(msg,'utf-8') + bytes(freshnessValue,'utf-8')+mac.digest()
	print(SecurePDU)
	return SecurePDU

def generateSecretKey():
	key = Fernet.generate_key()
	#print("Secret key : ",end='')
	#print(key,end='\n\n')
	return key
	
if __name__=='__main__':
	msg = 'Payload to Send'
	freshnessValue = FreshnessManager.getFreshnessValue()
	print('Freshness Value: %s'%freshnessValue)
	key = generateSecretKey()	
	mac = generateMAC(msg,key,freshnessValue)
	securePDU = generateSecurePDU(msg,freshnessValue,mac)
	FreshnessManager.incFreshnessCounter()
	print(securePDU)
