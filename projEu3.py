# github.com/Spokenlore

# ProjectEuler Problem 3
# Find the largest prime factor of the number 600851475143
# Answer: 6857

import time

def largestPrimeFactor(num):

    currentDiv = 3

    while (num != 1):
        while (num % currentDiv == 0):
            num = num/currentDiv
        print currentDiv
        currentDiv += 2
    return currentDiv

startTime = time.time()
answer = largestPrimeFactor(600851475143)
elapsedTime = (time.time() - startTime)

print "\n" "The answer is %s and the calculation took %s seconds" % (answer, elapsedTime)