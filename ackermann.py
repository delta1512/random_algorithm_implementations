import sys

def ackermann(m, n):
    if m == 0:
        return n + 1
    elif (m > 0) and (n == 0):
        return ackermann(m - 1, 1)
    elif (m > 0) and (n > 0):
        return ackermann(m - 1, ackermann(m, n - 1))


sys.setrecursionlimit(2**30)
print(ackermann(4, 1)) #Resulted in SEGFAULT
