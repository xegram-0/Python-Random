# Exercise 10: Generate a random date between given start and end dates


import time
import random

def get_random_date(startdate,enddate):
    # Uniform the format of the date
    dateFormat = "%d/%m/%Y"

    # Random element
    randomGen = random.random()
    
    # Convert my time into seconds?
    startTime = time.mktime(time.strptime(startdate,dateFormat))
    endTime = time.mktime(time.strptime(enddate,dateFormat))
    #print(startTime,endTime)

    # You make random time by using the equation below
    # The random element is used by multiplying the random with
    # the amount of time between starting time and ending time
    randomTime = startTime + randomGen * (endTime-startTime)
    # Convert the time into date
    randomDate = time.strftime(dateFormat,time.localtime(randomTime))
    #print(randomTime)
    return randomDate

def main():
    print("I picked a random date from 01/01/2001 to now 02/07/2023 (Eastern style)")
    print(f"My random date is {get_random_date("01/01/2001","02/07/2023")}")

if "__main__"==__name__:
    main()