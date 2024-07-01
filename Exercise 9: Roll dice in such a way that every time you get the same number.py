# Exercise 9: Roll dice in such a way that every time you get the same number
# I guess seed means key
# Each time change the seed value,
# The result will change
import random

dice:list = [1,2,3,4,5,6]
for i in range(5):
    random.seed(53)
    print(random.choice(dice))