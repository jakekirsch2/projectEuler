class problem9:
    def main():
        for a in range(1000):
            for b in range(1000 - a - 1):
                for c in range(1000 - a -b - 2):
                    if(a+1 + (b + 2) + (c + 3) == 1000 and (a+1)**2 + (b+2)**2 == (c+3)**2):
                        return (a+1) * (b+2) * (c+3)
print(problem9.main())