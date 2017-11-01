

def prob2(fiblimit):

    n1 = 1
    n0 = 1
    temp = 0
    sum = 0

    while n1 < fiblimit: 

        if n1%2 == 0:
            sum += n1
#don't need to save all the numbers
        temp = n1
        n1 = n1 + n0
        n0 = temp

    return sum

        

    
    
