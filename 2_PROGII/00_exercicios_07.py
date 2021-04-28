def primo (x):
    for i in range (1,x):
        if x%i==0:
            return False
        else:
            return True

print (primo(2))
