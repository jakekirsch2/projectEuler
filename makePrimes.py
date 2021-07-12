def main(max):
    primes = []
    listOfPrimes = []
    for i in range(2, max):
        primes.append([i, True])
    for i in range(len(primes)):
        if(primes[i][1] == True):
            listOfPrimes.append(primes[i][0])
            for j in range(0, len(primes) - i, primes[i][0]):
                if(j != 0):
                    primes[j+i][1] = False
    return listOfPrimes