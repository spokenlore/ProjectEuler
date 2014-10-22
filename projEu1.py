# github.com/Spokenlore

# ProjectEuler Problem 1
# Find the sum of all numbers divisible by 3 or 5 below 1000
# Answer: 233168

sum = 0
for x in range(0,1000):
    if (x%3 == 0 or x%5 == 0):
       sum += x
print sum