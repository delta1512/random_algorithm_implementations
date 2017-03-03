from math import ceil
from sys import argv, exit

factors = []

try:
    number = int(argv[1])
except:
    print('Invalid input: ', str(argv[1]))
    exit()

for i in range(1, ceil(number / 2)):
    if number % i == 0:
        res = [i, int(number / i)]
        free = True
        for x in factors:
            if len(factors) == 0:
                break
            elif res[1] == x[0]:
                free = False
                break
            else:
                free = True
        if free:
            factors.append(res)

for factor in factors:
    print(str(factor[0]) + '\tand\t' + str(factor[1]))
