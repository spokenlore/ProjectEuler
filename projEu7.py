# github.com/spokenlore
# ProjectEuler Problem 7

# What is the 10,001st prime number?
# Answer: 104743

import time
import sys
import os
from math import sqrt

def findPrime(nthTerm):
	currentNum = 2
	currentPrime = 1
	prime = True
	while (currentPrime <= nthTerm):
		if (currentNum == 2):
			# Base case hardcoded
			# print "%s %s" % (currentNum, currentPrime)
			currentPrime += 1
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
				if currentPrime == nthTerm:
					break
				currentPrime += 1
				currentNum += 1
			else:
				currentNum += 1
				prime = True
	return currentNum

startTime = time.time()
print findPrime(10001)
endTime = time.time()
totalTime = endTime - startTime
print "The program took %s seconds to run" % (totalTime)