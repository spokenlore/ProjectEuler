# github.com/spokenlore
# ProjectEuler Problem 10

# What is the sum of all prime numbers below 2 million?
# Answer: 142913828922

import time
import sys
from math import sqrt

def sumPrimes():
	currentNum = 2
	sumPrimes = 0
	prime = True
	while (currentNum <= 2000000):
		if (currentNum == 2):
			# Base case hardcoded
			# print "%s %s" % (currentNum, currentPrime)
			sumPrimes += currentNum
			currentNum += 1
		if (currentNum % 2 == 0):
			currentNum += 1
		else:
			for x in range(2, int(sqrt(currentNum))+1):
				if (currentNum % x == 0):
					prime = False
					break
			if (prime == True):
				# To output all primes up to target, uncomment below statement
				# print "%s %s" % (currentNum, currentPrime)
				sumPrimes += currentNum
				currentNum += 1
			else:
				currentNum += 1
				prime = True
	return sumPrimes

startTime = time.time()
print sumPrimes()
endTime = time.time()
totalTime = endTime - startTime
print "The program took %s seconds to run" % (totalTime)