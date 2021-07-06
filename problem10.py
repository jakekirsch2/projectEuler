import problem3

class problem10:
    def main():
        tempSum = 0
        primes = []
        for i in range(2, 2000000):
            primes.append([i, True])
        for i in range(len(primes)):
            if(primes[i][1] == True):
                tempSum = tempSum + primes[i][0]
                for j in range(0, len(primes) - i, primes[i][0]):
                    if(j != 0):
                        primes[j+i][1] = False

        return tempSum

print(problem10.main())

