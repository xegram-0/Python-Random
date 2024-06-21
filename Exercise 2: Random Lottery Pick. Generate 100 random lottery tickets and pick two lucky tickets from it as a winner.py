# Exercise 2: Random Lottery Pick. Generate 100 random lottery tickets and pick two lucky tickets from it as a winner.

# you must adhere to the following conditions:

#     The lottery number must be 10 digits long.
#     All 100 ticket number must be unique.
import random

lottery_list:list = random.sample(range(1000000000,9999999999),100)
winning_list:list = random.sample(lottery_list,2)
print(winning_list)