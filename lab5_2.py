

def counter(a, b):
    """
        Function, that takes 2 positive integers a and b
        Return the number - quantity of numbers b that a contain
    """
    matched = []
    #convert a and b to strings and append to matched the numbers that both of it has
    for j in str(b):
        if j in str(a):
            matched.append(j)
    #remove all duplicates of numbers in matched        
    for x in matched:
        while matched.count(x) > 1:
            matched.remove(x)
    return len(matched)           
        
