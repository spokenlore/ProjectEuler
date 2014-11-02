# github.com/spokenlore
# ProjectEuler Problem 5

# What is the smallest number evenly divisible by all numbers from 1-20
# Answer: 232792560

import time

# Returns GCD using Euclid's Algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Returns lowest common multiple of numbers a and b
def lcm(a, b):
    return a * b // gcd(a, b)

# Returns lowest common multiple of sequence, using previous lcm function
def lcm_seq(seq):
    return reduce(lcm, seq)

startTime = time.time()
solution = lcm_seq(xrange(1,21))
endTime = time.time()
totalTime = endTime - startTime
print "The answer is %s and calculations finished in %s seconds." % (solution, totalTime)