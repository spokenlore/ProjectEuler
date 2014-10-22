# github.com/Spokenlore

# ProjectEuler Problem 2
# Find the sum of all even-valued Fibonnaci sequence terms below 4 million
# Answer: 4613732

sum = 0
currentfib = 0
num1, num2 = 1, 1;
counter = 1;

while (currentfib < 4000000):
    if (counter % 2 == 0):
        currentfib = num1+num2
        num1 = currentfib
        counter += 1
    else:
        currentfib = num1+num2
        num2 = currentfib
        counter += 1
    print currentfib, "\n"
    if (currentfib %2 == 0):
        sum += currentfib
print sum