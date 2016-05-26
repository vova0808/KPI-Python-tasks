


def saddle_point(matrix):
    """
        Function, that takes a matrix as input and return a saddle point of this matrix.
        Saddle point is an element of matrix, that is stricly less than others in it's row
        and stricly bigger than others in it's column.
        Function return a tuple with coordinates of saddle point if it's appear in matrix or
        False if matrix has not saddle point.
        Matrix is a list of a lists.
        output is a tuple, where first number is index of a row in matrix, that containt saddle
        point, second number is index of saddle point in that row.
    """

    #first we check if matrix containt at lest two lists. If not, return (0,0)
    if len(matrix) == 1:
        return (0, 0)
    
    else:
        min_values = [] #list for minimum values in each row, and it's indeces
        max_values = [] #list for maximum values in each column, and indeces it's values
        
        saddle = []     #list to hold saddle point 

        #find a min value of each row and it column
        for row in matrix:
            minimum = min(row)    #set minimum value of each row to variable minimum
            if row.count(minimum) > 1: #check if that value is stricly less than others it it's row. If any element is equal to it, continue our search
                continue
            else:
                min_ind = row.index(minimum) # set index minimum value to variable min_ind
                min_values.append((minimum, min_ind, matrix.index(row))) #add that value, it index and row index to min_values list
            

        #find a max value of each column and it row    
        lst = zip(*matrix) # convert matrix to list of tuples, where every tuple contain one column of matrix in ascending order
        for col in lst:
            maximum = max(col) #set maximum value of each column to maximum
            if col.count(maximum) > 1: #cgeck ig that value is stricly bigger than others in column. If any element is equal to it, continue search
                continue
            else:    
                col_ind = lst.index(col) #set index of each column in lst to col-ind 
                max_values.append((maximum, col_ind)) #append maximum value of each column and index of that column to max_values
        #looking if value in max_values equal to the second and third elements of each values in min_values. If it is, append second and first elements to the saddle list
        for i in min_values:
            for j in max_values:
                if i[0:2] == j:
                    saddle.append(i[-1])
                    saddle.append(i[-2])
                
        if len(saddle) != 2: # if len saddle non equal to 2 it ,means there are at least zero or more than one saddle point in list. In this case return False
            return False
        else:
            return tuple(saddle)
        
    
                

        
            
        

             
            
        

       
                
        
            
                
         
        
                
        
        

        

                            
            
            


        

          
                        


       
           

        
            

        
            
                

            
            

            
        
                

            

        
            
             
                
            
                
        
                
                
                
        
        
       
        
                
           
    
    
        
    
            
                
