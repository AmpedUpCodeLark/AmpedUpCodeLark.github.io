# Head First Python - vowels code
# David Gillette
# 630-975-7282
# jupyter editor

# the "vowels" variable is assigned the list of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# the "word" variable is assigned the word "Millways"
word = "Milliways"

# checking for one object inside another object
# the for loop checks for each letter in the word variable
# assigning each letter to the letter variablbe
for letter in word:
    
# Checks to see if the letter assigned to letter variable
# from the word variable is found in the list assigned to vowels 
        if letter in vowels:
        
# if the letter from the word varibale is found in the vowels
# list then the letter is printed.
                print(letter)
