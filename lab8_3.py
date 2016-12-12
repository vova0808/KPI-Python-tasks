
def bouquets(narcissus_price, tulip_price, rose_price, summ):

    result = 0

    # find max q-ty of narcissus that we can buy
    max_narcissus = int(summ // narcissus_price)

    #find max q-ty of tulips that we can buy
    max_tulips = int(summ // tulip_price)

    #find max q-ty of roses that we can buy
    max_roses = int(summ // rose_price)

    for i in range(0, max_narcissus + 1):
        for j in range(0, max_tulips + 1):
            for k in range(0, max_roses + 1):
                if i * narcissus_price + j * tulip_price + k * rose_price <= summ:
                    if (i + j + k) % 2 != 0:
                        result += 1
                else:
                    break
    return result













print bouquets(2, 3, 4, 100)






    
    


        
            
    
        
