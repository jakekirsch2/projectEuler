import makePrimes
def main():
    index = 7
    triangleNumber = 28
    found = False
    primes = makePrimes.main(2000000)
    while not found:
        index = index + 1 
        triangleNumber = triangleNumber + index
        numberOfDivisors = getNumDivisors(triangleNumber,primes)
        if(numberOfDivisors > 500):
            print(triangleNumber)
            found = True

        
def getNumDivisors(number,primes):
    exponents = []
    tempNumber = number
    for prime in primes:
        numExponents = 0
        while tempNumber % prime == 0:
            numExponents = numExponents + 1
            tempNumber = tempNumber / prime
        if(numExponents > 0):
            exponents.append(numExponents + 1)
        if(prime > tempNumber):
            break
    totalDivisors = 1
    for exponent in exponents:
        totalDivisors = totalDivisors * exponent
        
    return totalDivisors


main()