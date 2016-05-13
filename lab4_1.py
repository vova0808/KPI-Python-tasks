"""
Ptogram takes input as command line argument.
Input is a string, that can containe a spaces, letters in any register and numbers
If input is a palindrome, return YES, else - return NO
"""


import sys
user_input = sys.argv[1]

#convert input to list
user_input = list(user_input)

#iterate over list, and looking for a spaces and removing all of them
for i in user_input:
    if i == " ":
        user_input.remove(i)

#convert input to a string        
user_input = "".join(user_input)

#convert input in a lower register
user_input = user_input.lower()

#make a copy of user input and compare it with input. 
rev_input = user_input[::-1]
if user_input == rev_input:
    print "YES"
else:
    print "NO"
    

    
    
        


        

    
