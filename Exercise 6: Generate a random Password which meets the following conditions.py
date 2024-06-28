# Exercise 6: Generate a random Password which meets the following conditions
# Conditions:
#    Password length must be 10 characters long.
#    It must contain at least 2 upper case letters, 1 digit, and 1 special symbol.


import string
import random

def make_password():
    # Make a pool of random stuff for the remaining 6 characters
    random_mix = string.ascii_letters + string.digits + string.punctuation
    samplePassword = random.sample(random_mix,6)
    # Fill the remaining requirements
    samplePassword += random.sample(string.ascii_uppercase,2)
    samplePassword += random.choice(string.digits)
    samplePassword += random.choice(string.punctuation)
    # Make a list of the sample in order to shuffle the elements in the list
    listPassword = list(samplePassword)
    # Shuffle it
    random.SystemRandom().shuffle(listPassword)
    # Then join the element of the list into a string
    password = ''.join(listPassword)
    return password
def main():
    password:str = make_password()
    print("Your password is" + password)


if "__main__" == __name__:
    main()