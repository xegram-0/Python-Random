# Exercise 1: Generate 3 random integers between 100 and 999 which is divisible by 5

import random

result = []
for i in range(3):
    result.append(random.randrange(100,999,5))
print(result)

# No need for list