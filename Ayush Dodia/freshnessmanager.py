def getFV():
	with open('Counter.txt') as fi:
		return fi.read()

def incFV():
	fi = open("Counter.txt")
	count = int(fi.read())
	count +=1
	fi.close()
	setFV(count)
	
def setFV(count):
	with open('Counter.txt','w') as fi:
		fi.write(str(count))	

def resetFV():
	setFV(0)

if __name__=='__main__':
	resetFV()
