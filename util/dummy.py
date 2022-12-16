import random

rand_1 = random.uniform(0, 50)
rand_2 = random.uniform(0, 50)
print("Random number 1 is: " + str(rand_1))
print("Random number 2 is: " + str(rand_2))
print("Highest value is: " + str(max(round(rand_1), round(rand_2))))
