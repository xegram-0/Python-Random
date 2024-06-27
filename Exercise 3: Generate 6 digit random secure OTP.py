# Exercise 3: Generate 6 digit random secure OTP

import random
import secrets

secret_gen = secrets.SystemRandom()
secret_num = secret_gen.randrange(100000,999999)
print(secret_num)