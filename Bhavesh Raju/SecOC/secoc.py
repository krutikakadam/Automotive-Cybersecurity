from cryptography.fernet import Fernet
import string
import random
import time
i=0
count=float(5005)
while i<10:
#key
  password="hEuziQP32kugta0xDIy3JaF64UYqjvG8W20n60vBVdM="
  enpass=password.encode()
  fernet = Fernet(enpass)
#data or payload
  N = 2
  res = ''.join(random.choices(string.ascii_uppercase +string.digits, k=N))
  res1 = ''.join(format(ord(i), '08b') for i in res)
  #print(type(res1))
  endata= fernet.encrypt(res1.encode())
  endata1=endata.decode()
#counter 
  count+=0.05
  freshness_value = str(count)
#print(endata1)
#print(freshness_value)
#print(len(freshness_value))
#SecOC
  SecOC=res1+endata1+freshness_value
  secoc=SecOC.encode()
  time.sleep(1)
  print(secoc)
  i+=1
