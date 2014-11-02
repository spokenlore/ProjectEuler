# github.com/Spokenlore

# ProjectEuler Problem 1
# Find the sum of all numbers divisible by 3 or 5 below 1000
# Answer: 233168

import time

def sumDivisible(num, div1, div2):
    sum = 0
    for x in range(0,num):
        if (x%div1 == 0 or x%div2 == 0):
           sum += x
    return sum

startTime = time.time()
answer = sumDivisible(1000, 3, 5)
endTime = time.time()

print  '\n' "The answer is %s and the calculations took %s seconds." % (answer, endTime-startTime)