
def convert_n_to_m(x, n , m):
    """
        Function, that takes three arguments as input:
        x - an integer, in notation with the n-th base, or a string, that represents this number
        integers n and m (1<=n, m<=36)
        Return a string, that represents x in a m-th notation
        If x is not an integer or string, or cannot be represent as positive number
        if notation with base m, return False.
        Assume, that in notation with the base of 1, number will write appropriate q-ty of zeros
        

    """
    #variable to hold all symbols to write representation of any number with all notation
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    tmp = []
    assert n >= 1 and m <= 36

    #if type x is not integer or float, return False
    if type(x) == list or type(x) == dict or type(x) == tuple or type(x) == float:
        return False

    #helper function for converting x to integer with base n
    def to_int(x, n):
        x = str(x)
        try:
            x = int(x, base = n)
            return x
        except:
            return False
    
    x = to_int(x, n)    

    #if result of to_int equal to zero return x, if less than zero, return False
    if x == 0:
        return x
    elif x < 0:
        return False
    #if m == 1, return equal quantity of zeros multiplied to result of to_int of x
    elif m == 1:
        return "0" * x
    elif x == False:
        return x
        
    else:
        #add to tmp element which index is modulo of x % m 
        while x != 0:
            tmp.append(chars[x % m])
            #update x
            x /= m
            if x < m:
                #when x less than m, add to tmp element which index is x
                tmp.append(chars[x])
                #set x to zero for exit from cycle
                x -= x
    #reverse tmp, convert it to string and return it            
    tmp = tmp[::-1]
    return "".join(tmp)
            
          
            
    
        
    
    
            
    
            
        
            
