

def prob5v1():

    lcm = 2520

    while notDivisible(lcm):
        lcm+=2520

    return lcm


def notDivisible(lcm):

    for i in range(1,20):
        if lcm%i != 0:
            return 1

    return 0


def prob5v2():

    """Find all primes below n (going to be lazy about this)
        Go through all numbers below n and see their prime factorization.
        Count out how many of each prime, if greater than current, add.
        Store numbers in a list of tuples."""

    return 0

def primeFactors(n):

    factors = []
    lim = int(n**5)
    
    for i in range(2,lim+1):
        if n%i == 0:
            factors += [i,n/i]
            
    factors.sort()

    for j in range(0,len(factors)):
        if isPrime(factors[j]) == 0:
            factors[j] = primeFactors(factors[j])
            

    return factors
        


def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return 0

    return 1
