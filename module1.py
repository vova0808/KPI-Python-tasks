"""
Programm, that decrypting message using Francis Bacon code
"""



import sys


key = 'aaaaabbbbbabbbaabbababbaaababaab'
alphabet = 'abcdefghijklmnopqrstuvwxyz'
message = sys.argv[1]

#create an empty string for end result
result = ""


#split for groups with 5 symbols length, deleting all spaces
sequence = []
message = message.replace(" ", "")
for i in range(0, len(message), 5):
    sequence.append(message[i:i+5])


# deleting elements with length less than 5
for i in sequence:
    if len(i) != 5:
        sequence.remove(i)


#lower register symbols transform to 'a', upper - to be 'b' and adding to new list ab
ab = [] # list for sequence a-b-symbols
for i in sequence:
    for j in i:
        if j.islower():
            j = "a"
        else:
            j = "b"
        ab.append(j)
        
ab_five = [] #list with ab-words with 5 symbols length

#adding 5-symbols length ab-words to ab_five
for i in range(0, len(ab), 5):
    ab_five.append(ab[i:i+5])

coded = [] # list for converting sublists in ab_five to string withwords
for i in ab_five:
    coded.append("".join(i))
coded = "".join(coded)

#decoding using key
for i in range(0, len(coded), 5):
    coded_part = coded[i:i+5]
    if len(coded_part) == 5:
        letter = alphabet[key.find(coded_part)]
        result += letter
print result    
   

    

        






         

            
        
   
    



    
   
    
    
    





        
        

  
