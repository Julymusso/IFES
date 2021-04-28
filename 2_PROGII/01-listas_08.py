def fibonacci (n):
    l=[1]
    for i in range (1,n):
        l.append(l[i-1]+l[i-2])
    return l


print (fibonacci(6))
