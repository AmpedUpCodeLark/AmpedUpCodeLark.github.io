# Head First Python - beer code
# David Gillette
# 630-975-7282
# jupyter editor

# Import the time module
import time

# The variable called "word" is assigned the string value "bottles"
word = "bottles"

# Using the range function with three arguments of start, stop and step,
# the "for" loop specifies from 99 to none using beer_num as the
# iteration variable
for beer_num in range(99, 0, -1):
    
# print beer_num iteration variable (first iteration "99"
# print the variable called "word" which equals "bottles"
# print the text "of beer on the wall.")
    print(beer_num, word, "of beer on the wall.")
    
# print beer_num iteration variable (first iteration "99"
# print the variable called "word" whihc is equal to "bottles"
# print the text "of beer.")
    print(beer_num, word, "of beer.")
    
# print the text "Take one down."
    print("Take one down.")
    
# print the text "Pass it around."
    print("Pass it around.")
    
# if statement checks if the iteration variable beer_num is
# equal to 1 (Note the "=" is an assigment operator while
# the "==" is a comparison operator)
    if beer_num == 1:
        
# If the beer _num iteration variable is 1 then print the text
# "no more bottles of beer on the wall."
        print("No more bottles of beer on the wall.")
    
# Else if beer_num iteration variable is not equal 1 continue 
    else:

# beer_num iteration variable is reduce by 1 and assigned to the
# new_num variable
        new_num = beer_num - 1
    
# if the new_num variable equals the number 1 the if statement changes
# the word variable to "bottle" singular from "bottles" plural
        if new_num == 1:
            word = "bottle"
            
# print "1 bottle of beer on the wall."
        print(new_num, word, "of beer on the wall.")
        
# time.sleep inserted to pause 2 seconds use you can see execution of 
# program output in sequence
        time.sleep(1)
    
# print one last blank line when all the iterations are completed
    print()
