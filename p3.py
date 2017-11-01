

def prob3(n):

    factors = []
    factors2 = []
    lim = int(n**.5)

    #also need to check other divisor

    for i in range(2,lim+1): 
        if n%(i)==0: #gives factors, adding 2 because lim can be prime
            factors += [i]
            factors2 += [n/i]

    totalFactors = factors + factors2[::-1]
    totalFactors = totalFactors[::-1]

    for i in range(0,len(totalFactors)):
        if isPrime(totalFactors[i]):
            return totalFactors[i]

    return 1
            

def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0

    return 1
