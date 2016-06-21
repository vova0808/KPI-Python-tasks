"""
Program, that is looking for 'happy' tickets.
'Happy' ticket is a trolley bus ticket, in which sum of first three numbers is
equal to the sum of last three numbers.
Input data: two integers, command line arguments, 0<=a1<=a2<=999999
Output: quantity of 'happy tickets', which numbers lays on the interval from a1 to a2 including.
If number in the interval has less than 6 digits, consider that at the beginning
this number has a necessary quantity of zeros.
"""


import sys
a1 = int(sys.argv[1])
a2 = int(sys.argv[2])

#create a range of numbers between a1 and a2 
numbers = range(a1, a2+1)
tmp = []
#create a list for numbers, which length equal 6
working_list = []
#list for lucky numbers
lucky_numbers = []

#convert any number in numbers to a atring and append it to tmp
for i in numbers:
    tmp.append(str(i))

#if number has less than 6 digits, add necessary q-ty of zero's to it's beginning
for i in tmp:
    while len(i) < 6:
        i = "0" + i
    working_list.append(i)

#for ticket number in working list:
for char in working_list:
    #slice this number to 2 equal parts, number1 and number2
    number1 = str(char[0:3])
    number2 = str(char[3:])
    #variable to hold value of the sum first three numbers of ticket number
    total1 = 0
    #variable to hold value of the sum of last three numbers of ticket number
    total2 = 0
    #for digits in number1, convert it to int, and add to total1
    for x in number1:
        x = int(x)
        total1 += x
    #do the same for digits in number2   
    for y in number2:
        y = int(y)
        total2 += y
    #check, if number1 is equal to number2, add char to lucky_numbers    
    if total1 == total2:
        lucky_numbers.append(char)
print len(lucky_numbers)        

    
    
    
                         
             
    
    
    



    
    

        
    
    
    

    



    
    
    

   
        
    
    
    

        
    

