def getFreshnessValue():
	with open('FreshnessCounter.txt') as fi:
		return fi.read()

def incFreshnessCounter():
	fi = open("FreshnessCounter.txt")
	count = int(fi.read())
	count +=1
	fi.close()
	setFreshnessValue(count)
	
def setFreshnessValue(count):
	with open('FreshnessCounter.txt','w') as fi:
		fi.write(str(count))	

def resetFreshnessCounter():
	setFreshnessValue(0)

if __name__=='__main__':
	resetFreshnessCounter()