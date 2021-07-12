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
    primeFactors = []
    numToDivide = 1
    tempNumber = number
    for prime in primes:
        numRepeating = 0
        while tempNumber % prime == 0:
            numRepeating = numRepeating + 1
            tempNumber = tempNumber / prime
            primeFactors.append(prime)
        if(numRepeating >= 2):
            numToDivide = numToDivide * numRepeating 
        if(prime > tempNumber):
            break
        
    return 2**len(primeFactors) / numToDivide


main()