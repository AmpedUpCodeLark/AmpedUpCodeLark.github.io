# Head First Python - odds with detailed description
# David Gillette
# 630-975-7282
# jupyter editor

# The datetime submodule (after the import) is imported from the standard datetime module
# other submodule types are: date, time, timedelta, tzinfo, & timezone
from datetime import datetime

# random is the module that implments the pseudo-random number generators
# Allmost all module functions depend on the basic function of random()
import random

# time is the module that provides a function for getting local time from
#the number of seconds elapsed since epoch called localtime()
import time

# imports should be on the top of the code with each import on a separate line
# which is a well established convention


# A variable called 'odds' is created assigning a list of off nnumbers 1 through 59
odds = [1, 3, 5, 7, 9, 11, 13, 15 ,17, 19,
        21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
        41, 43, 45, 47, 49, 51, 53, 55, 57, 59]

# The "for i in range(5):" determines the number of times you want a suite of code to run
# i keeps track of the iterations and range() is a built in function. The colon ":"
# introduces a new suite of code. The suite of code must be indented or the interpreter
# rasies an error.
for i in range(5):

# right_this_minutes is the variable taking on the current minute from datetime.today().minute
    right_this_minute = datetime.today().minute

# The if statement evaluates if the variable assigned to right_this_minute is in the list odds
# If the minute IS in the odds list the next suite of code starting with print executes
    if right_this_minute in odds:
        print("The odds might be with us!")

# If the minute IS NOT in the odds list the suite of code under else: executes
    else:
        print("On second thought; the odds aren't with us!")

# wait_time is assigned a random number between 1 and 60 using the randint function
# of the random module
    wait_time = random.randint(1,60)
    
# time.sleep uses the sleep function of the time module to pause of wait the
# integter assigned to wait_time
    time.sleep(wait_time)
    
    