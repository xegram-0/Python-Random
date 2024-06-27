# Exercise 5: Generate random String of length 5
# Note: String must be the combination of the UPPER case and lower case letters only. 
# No numbers and a special symbol.

import string
import random


def get_string_of_5():
    letter_pool = string.ascii_letters
    random_str = ''.join(random.choice(letter_pool) for i in range(5))
    print(f"Your random string of length 5 is {random_str}")

def main():
    get_string_of_5()
if "__main__" == __name__:
    main()