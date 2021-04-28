def MDC(m,n):
    if m>n:
        maior=m
        menor=n
    else:
        maior=n
        menor=m
    
    while menor > 0:
        resto=maior%menor
        maior=menor
        menor=resto

    return maior