# Head First Python - panic with detailed description
# David Gillette
# 630-975-7282
# jupyter editor


# the string "Don't panic!" is assigned to the variable "phrase"
phrase = "Don't panic!"

# the string in the variable "phrase" is turned into a list
# and assigned to the variable "plist"
plist = list(phrase)

# the variable "phrase" and "plist" are printed visually
# validating the string and the list
print(phrase)
print(plist)

## manipulates the list not the string

# the "i" variable holds the iteration for the last four (4)
# elements of the variable "plist" using .pop()
for i in range(4):
    
# plist.pop() remove one element from the end of the
# variable "plist"
    plist.pop()
    
# using the list methhod pop() with an index of zero (0) plist.pop(0)
# removes the element "D" from the variable plist.
plist.pop(0)

# using the list method remove() the "'" is removed by searching
# through the elements of the variable "plist" for the specific value
plist.remove("'")

# combining the list method extend() and list method pop on
# the variable plist. plist is extended by two (2) pop()'s.
# Note that the the "p" element is popped first then the "a" element
# is popped. The when the variable extended the "a" element is added
# first then the "p" element is added
plist.extend([plist.pop(), plist.pop()])

# combing the list insert method and the list pop method along
# the index argument of the list insert method  and the index
# argument of the pop method the space element is popped from the
# plist at index of three (3) and inserted in plist at the index
# of two (2)
plist.insert(2, plist.pop(3))

# the variable new_phrase is assigned the result of the string method
# of join to concatenate the the elements of the variable plist
new_phrase = ''.join(plist)

# the variable "plist" and "new_phrase" are printed visually
# validating the strings
print(plist)
print(new_phrase)
