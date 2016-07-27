def file_search(folder, filename):
    """
        Function that takes 2 arguments - a list folder and string filename
        Return a string - a complete path to a file or folder filename in folder structure
    """
    #set initial value of path to a starting element of folder list
    path = folder[0] + "/"
    #if looking element is in a same folder, return path + name of element
    for i in folder[1:]:
        if i == filename:
            
            return path + str(filename)
        
        elif i != filename:
            #if folder contain any other folders
            if type(i) == list:
                #set new_path vaeriable to a recursive call of file_search
                new_path = file_search(i, filename)
                #if new_path find looking element
                if new_path != False:
                    #update the value of path, adding new_path to it and return it
                    path = path + new_path
                    return path
    return False            
        
                        
                            
                        

        
