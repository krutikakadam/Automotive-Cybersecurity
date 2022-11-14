import cryptography 
import freshnessmanager
from cryptography.fernet import Fernet
#from collection import counter 
import pyAesCrypt,os

Master_ID=int(input("ECU_ID for access :"))
file=open('ECU_ID')
Master_id=file.read()
file.close
if Master_ID==int(Master_id):
  print("AUTHENTICATION CONFIRMED")
  file=open('encrypted_data','rb')
  encrypted=file.read()
  print('Data from MASTER:',encrypted)
  #key1=str(input("Enter key for decryption :"))
  password="1234"
  password1=input("Enter password for key access: ")
  buffersize=256*1024
  if password1==password:
    pyAesCrypt.decryptFile("key_value.aes","key_valueout",password,buffersize)
    print("File decrypted")
    file=open('key_valueout','rb')
    key_data=file.read()
    print("key is:",key_data)
  else:
    print("No access to key flie")
  key1=str(input("Enter key for decryption :"))
  file=open('key_valueout','rb')
  key=file.read()
  file.close
  f1=Fernet(key)
  if key1==str(key):
     file=open('encrypted_data','rb')
     encrypted=file.read()
     decrypted=f1.decrypt(encrypted)
     original_data=decrypted.decode()
     print ("Decrypted Data:",original_data)
     fv = freshnessmanager.getFV()
     print('Freshness Value: %s'%fv)
     freshnessmanager.incFV()
  else:
     print("INVALID KEY")
     
else:
  print("UNAUTHORIZED ACCESS")

