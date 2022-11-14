import freshnessmanager
import hmac
import hashlib
from cryptography.fernet import Fernet	

def generateSKey():
	key=Fernet.generate_key()
	return key

def generateMAC(message,key,fv):
	payload= bytes(message,'utf-8') + key + bytes(fv,'utf-8')
	mac = hmac.new(key,payload, hashlib.sha1)
	return mac

def generateSPDU(message,fv,mac):
	SPDU = bytes(message,'utf-8') + bytes(fv,'utf-8') + mac.digest()
	return SPDU


	
if __name__=='__main__':
	message = 'Secure on board'
	fv = freshnessmanager.getFV()
	print('Freshness Value: %s'%fv)
	key = generateSKey()	
	mac = generateMAC(message,key,fv)
	SPDU = generateSPDU(message,fv,mac)
	freshnessmanager.incFV()
	print(SPDU)
