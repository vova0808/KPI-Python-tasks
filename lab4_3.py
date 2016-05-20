""" This program takes  input as a command line argument.
Input is a string, that consists of openings and
closings parenthesees. If input containing right sequence of parenthesees,
program return "YES", else return "NO"
"""

import sys
user_input = sys.argv[1] 
count = 0

#boolean variable for tracking if quantity of openings is in respect of quantity of closings 
matched = True 

#iterate over string and counting both opening and closing parenthesis
for i in user_input:
    if i == "(":
        count += 1
    elif i == ")":
        count -= 1
    # if count is less that 0 it means that quantity of closing parenthesis are greater than opening, so matched will be False 
    if count < 0:
        matched = False
        
#check if we have opening bracket at the start of string and closing in the end. 
if user_input[0] == ")" or user_input[-1] == "(":
    matched = False

#if quantity of closings and closings parenthesis are equal and matched, return True
if count == 0 and matched == True:
    print "YES"
else:
    print "NO"



    
            
