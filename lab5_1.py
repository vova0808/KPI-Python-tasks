def clean_list(list_to_clean):
    """
        Function, that takes 1 argument - a list of any values
        (a strings, integers or floats) arbitrary length
        Return a list, that contain exatly the same values, but without
        any repeats of elemnts
    """
    unique = [] #list for unique elements
    lst2 = []   #list for where all elements with type string
                #created to check and remove duplicates like 1.0 and "1.0"
    result = []
    #iterate over list_to_clean and convert every float element to string 
    for i in list_to_clean:
        if type(i) == float:
            i = str(i)
        #append that element to lst2    
        lst2.append(i)
    #add elements from lst 2 that are not in unique to unique    
    for i in lst2:
        if i not in unique:
            unique.append(i)
    for i in unique:
        #convert elements which were converted to a string for check their duplicates in other types 
        if type(i) == str and i not in list_to_clean:
            i = float(i)
        result.append(i)    
    return result      
        
