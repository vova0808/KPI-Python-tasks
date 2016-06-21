def count_holes(n):
    """
        Function, that takes one argument as it's input - an integer or a string, that represent that integer
        Return integer, that represent number of holes in decimal representation of it number
        Consider, that  4 and 0 both has one hole
        If argument not a number or haven't any holes, return ERROR
    """
    count = 0
    
    lst= []
    #built-in function that check if input str have any digits inside
    def count_digits(string):
        flag = False
        for i in string:
            if i.isdigit():
                flag = True
        return flag        

    #if it is floating number return error
    if type(n) == float:
        return "ERROR"
    #if it list return error
    elif type(n) == list:
        return "ERROR"
    #if it str first check if it have any points inside that may say us so that is float number
    elif type(n) == str:
        for i in n:
            if i == ".":
                return "ERROR"
    #if it not has any points inside check it with count_digits to see if it has any numbers inside        
        if count_digits(n) == False:
            return "ERROR"
        else:
            pass

    #if function has't any input or input equal None return error
    elif n == None:
        return "ERROR"
    #if input equal empty string return error
    elif n == "":
        return "ERROR"

    #else convert input to string and check if it first item equal zero
    n = str(n)
    for i in n:
        if i[0] == "0": #if it is, then convert it to integer
            n = int(n)
            n = str(n) #after convert to string again 
    lst.append(n)     #append it to empty list lst
    for i in lst:     #iterate over lst, then iterate over item in lst
        for j in i: #if item has any holes inside, adding respective number to count
            if j == "0" or j == "4" or j == "9" or j == "6":
                count += 1
            elif j == "8":
                count += 2
    return count            
            
                
                
            
                
    
                
                    
       
            
                
        
   

   
                    
                
