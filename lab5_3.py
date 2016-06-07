def super_fibonacci(n, m):
    """
        Function, that takes 2 arguments - integers m and n, (0 < n, m <= 35),
        and returns a number - n-th element of super-Fibonacci sequence of order m
        Super-Fibonacci sequence it's a sequence of numbers, where every element is
        equal to the sum of m previous elements.
        First m elements (with order numbers from 1 to m ) considering as 1
    """
    assert n > 0 and m <= 35
    count = 0 
    result = []
    for num in range(m):
        #add ones to the result in the range of m
        result.append(1)
        count += 1
    while count < n:
        #next, add sum of last m elements to the end of result
        result.append(sum(result[-m:]))
        count += 1
        
    return result[n-1]    
