import random

# Using randrange() to generate numbers from 0-100
print("Random number from 0-100 is : ", end="")
print(random.randrange(100))

# Using randrange() to generate numbers from 50-100
print("Random number from 50-100 is : ", end="")
print(random.randrange(50, 100))

# Using randrange() to generate numbers from 50-100
# skipping 5
print("Random number from 50-100 skip 5 is : ", end="")
print(random.randrange(50, 100, 5))


# Generates a random number between
# a given positive range
r1 = random.randint(0, 10)
print("Random number between 0 and 10 is % s" % (r1))

# Generates a random number between
# two given negative range
r2 = random.randint(-10, -1)
print("Random number between -10 and -1 is % d" % (r2))

# Generates a random number between
# a positive and a negative range
r3 = random.randint(-5, 5)
print("Random number between -5 and 5 is % d" % (r3))


# initializing list
test_list = [1, 4, 5, 6, 3]

# Printing original list
print("The original list is : " + str(test_list))

# using random.shuffle()
# to shuffle a list
test_copy = test_list[:]
random.shuffle(test_copy)  # no return value, shuffles list in the process

# Printing shuffled list
print("The shuffled list is : " + str(test_copy))

# random.choice() select random item from the list
list = [111, 222, 333, 444, 555]
print("random.choice() to select random item from list - ", random.choice(list))
print("random.choice() to select random item from list - ", random.choice(list))
