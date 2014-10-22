# github.com/Spokenlore
# ProjectEuler Problem 4

# Find the largest palindrome made from the product of two 3-digit numbers
# Answer:

import time

def checkPalindrome(num):
    originalNum = num
    reversedNum = 0
    while (originalNum > 0):
        digit = originalNum % 10
        reversedNum = reversedNum*10 + digit
        originalNum = originalNum/10
    if (num == reversedNum):
        return True
    else:
        return False

def largestPalindromeProduct(num):
    a = num
    b = num
    maxPalindrome = 0
    product = a*b
    while a > 99:
        b = 999
        while b >= a:
            product = a*b
            if (product > maxPalindrome and checkPalindrome(product)):
                maxPalindrome = product
            b -= 1
        a -= 1

    return maxPalindrome

startTime = time.time()
answer = largestPalindromeProduct(999)
elapsedTime = (time.time() - startTime)

print "\n" "The answer is %s and the calculation took %s seconds" % (answer, elapsedTime)