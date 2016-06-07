morse_code = {
    "A" : ".-", 
    "B" : "-...", 
    "C" : "-.-.", 
    "D" : "-..", 
    "E" : ".", 
    "F" : "..-.", 
    "G" : "--.", 
    "H" : "....", 
    "I" : "..", 
    "J" : ".---", 
    "K" : "-.-", 
    "L" : ".-..", 
    "M" : "--", 
    "N" : "-.", 
    "O" : "---", 
    "P" : ".--.", 
    "Q" : "--.-", 
    "R" : ".-.", 
    "S" : "...", 
    "T" : "-", 
    "U" : "..-", 
    "V" : "...-", 
    "W" : ".--", 
    "X" : "-..-", 
    "Y" : "-.--", 
    "Z" : "--.."
    
}

def encode_morze(text):
    """
        Function, that takes 1 argument - a string.
        Return string of characters, that contains diagram of signal, that is respective to
        transmitted string coded in Morze.
        Pay no attention to the punctuation characters and to the others characters that are not in English alphabet
    """
    result = [] # list for output
    tmp1 = [] #list for letters in upper register and spaces
    tmp2 = [] #list for morzed letters and spaces
    tmp3 = [] # list for morzed letters with additional spaces between letters

    # iterate over text and if text have any digits return blank output
    for i in text:
        if i.isdigit():
            return ""

    # check if text has any characters, and if it has't return blank output   
    if len(text) == 0:
        return ""
    else:
        text = list(text) #convert text into list
        for i in text:    #iterate over text
            if i.isalpha(): #check if element is a letter
                tmp1.append(i.upper()) # if ist is, convert it to uppercase register and add it to tmp1 list
            elif i == " ": # if element is a space between words, add it to tmp1 as is
                tmp1.append(i)
            else: # all other elements passed
                pass
    #iterate over tmp1
    for i in tmp1:
        if i in morse_code: #check if item in tmp1 is equal to one of the keys in morse_code
            tmp2.append(morse_code[i]) # if it is, append to tmp2 value from respective key from morse_code
        else:
            tmp2.append(i) #in other hand, add it to tmp2 as is

    #iterate over tmp2, concantenate every elemnt with __ and append it to tmp3
    for elem in tmp2:
        tmp3.append(elem + "__")

    #convert tmp3 to string
    tmp3 = "".join(tmp3)

    #convert tmp3 to list
    tmp3 = list(tmp3)

    #iterate over tmp3, encrypt his elemnts and add it to result
    for char in tmp3:
        if char == " ":
            result.append("__")
        elif char == ".":
            result.append("^_")
        elif char == "-":
            result.append("^^^_")
        else:
            result.append(char)
    result = "".join(result)
    result = list(result)
    result = result[:-3] #delete extra elements from the end of result
    return "".join(result)
        
              
                
  
   
             
                

            
            
    
        
