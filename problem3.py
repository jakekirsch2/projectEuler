import math

class problem3:
    def isPrime(number, primes):
        for i in primes:
            if(number % i == 0):
                return False
        return True
    def main():
        mainNum = 600851475143
        primes = [2,3]
        topNumber = math.floor(mainNum / 3)
        biggestNumber = 3
        i = 5
        while i < topNumber:
            if(problem3.isPrime(i, primes)):
                primes.append(i)
                if(mainNum % i == 0):
                    topNumber = mainNum / i
                    biggestNumber = i
            i = i + 1
        return biggestNumber

# print(problem3.main())