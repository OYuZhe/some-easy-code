MaxLen = 10000000

#init Array
primeArray = [1]*10250000
primeArray[0]=0
primeArray[1]=0


def findPrime():
#sieve of Eratosthenes
	for i in range(0,3200):
		if primeArray[i] == 1:
			mul = 2
			IsNotPrime = i * mul
			while IsNotPrime <= MaxLen:
				IsNotPrime = i * mul
				primeArray[IsNotPrime]=0
				mul += 1

def printPrime():
#print prime
	for i in range(0,MaxLen):
		if primeArray[i] == 1:
			print(i)
			
if __name__ == '__main__':
	findPrime()
	printPrime()
