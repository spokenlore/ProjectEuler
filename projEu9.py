# github.com/spokenlore
# Project Euler Problem 9

# Find the pythagorean triplet where a+b+c = 1000, and calculate a*b*c
# Answer: 375, 200, 425

import time
from math import sqrt

def main():
	a = 1 
	b = 1
	c = 1
	numLoops = 0
	answerFound = False
	while (answerFound == False):
		c = sqrt(a*a + b*b)
		# if isinstance(c, int):
		# print "Current C is %s" % (c)
		if (a+b+c == 1000):
				answerFound = True
		else:
			if (a+b+c > 1000):
				b += 1
				a = 1
			else:
				a += 1
		if b > 1000:
			break
	return (a, b, c)

startTime = time.time()
answers = main()
endTime = time.time()

print "The answers are %s, and the calculations took %s seconds" % (answers, endTime-startTime)