# github.com/spokenlore
# Project Euler Problem # 11

# Find the largest number that can be found by multiplying 4 numbers in the given matrix
# Answer: 70600674

import time
import io

def separate(filename):
    all_integers = []
    with open(filename) as myfile:
        for line in myfile:
            for item in line.split(' '):
                    # Try converting the item to an integer
                    value = int(item, 10)
                    all_integers.append(value)
    return all_integers

def slice_list(input, size):
    input_size = len(input)
    slice_size = input_size / size
    remain = input_size % size
    result = []
    iterator = iter(input)
    for i in range(size):
        result.append([])
        for j in range(slice_size):
            result[i].append(iterator.next())
        if remain:
            result[i].append(iterator.next())
            remain -= 1
    return result

def largestProduct(list):
	largest = 0
	for x in xrange(0, len(list)):
		for y in xrange(0, len(list[x])):
			# Vertical Product
			if x < 17:
				product = list[x][y] * list[x+1][y] * list[x+2][y] * list[x+3][y]
				if product > largest:
					largest = product
			# Horizontal Product
			if y < 17:
				product = list[x][y] * list[x][y+1] * list[x][y+2] * list[x][y+3]
				if product > largest:
					largest = product
			# Diagonal SE
			if x < 17 and y < 17:
				product = list[x][y] * list[x+1][y+1] * list[x+2][y+2] * list[x+3][y+3]
				if product > largest:
					largest = product
			# Diagonal SW
			if x < 17 and y > 3:
				product = list[x][y] * list[x+1][y-1] * list[x+2][y-2] * list[x+3][y-3]
				if product > largest:
					largest = product
	return largest

startTime = time.time()
numList = slice_list(separate("nums.txt"), 20)
answer = largestProduct(numList)
endTime = time.time()

print "The answer is %s and the calculations took %s seconds" % (answer, endTime-startTime)