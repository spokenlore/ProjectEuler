# github.com/spokenlore
# ProjectEuler Problem 6

# Find the difference between the sum of the squares of the first hundred natural numbers and the square of the sum
# Answer: 25164150

import time

def sumSquares(min, max):
	sum = 0
	for x in range(min, max+1):
		sum += x*x
	return sum

def squareSum(min, max):
	sum = 0
	for x in range (min, max+1):
		sum += x
	return sum*sum

startTime = time.time()
answer = squareSum(1,100) - sumSquares(1,100)
endTime = time.time()

totalTime = endTime - startTime

print "The answer is %s, and the calculations took %s seconds" % (answer, totalTime)