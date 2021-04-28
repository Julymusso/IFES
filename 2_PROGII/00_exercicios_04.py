def divisor(x,y):
    if (y % x == 0):
        return True
    return False

n1 = int(input())
n2 = int(input())
print (divisor(n1,n2))