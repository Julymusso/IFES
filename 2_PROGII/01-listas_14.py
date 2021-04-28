def salario (n):
    func=[]
    sal=[]
    for r in range (n):
        func.append(input("Nome: "))
        sal.append(int(input("Salário: ")))
    media=sum(sal)/n
    for r in range (n):
        if sal[r]>=media:
            print ("\n\nFuncionário:",func[r],"\nSalário:",sal[r])

salario(5)
