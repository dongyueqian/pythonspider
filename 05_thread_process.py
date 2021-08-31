import math

def fn(n):
    if n<2:
        return False
    if n==2:
        return True
    if n % 2 == 0:
        return False

    sq = int(math.floor(math.sqrt(n)))
    for i in range(3,sq+1,1):
        print(i,'------')
        a = n % i
        print(a)
    # return sq

print(fn(27))

# for i in range(3,4,2):
#     print(i)

