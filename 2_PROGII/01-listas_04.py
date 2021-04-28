def ocorrencias (x,listaN):
    ocorrenciaN = listaN.count(x)
    return ocorrenciaN

oco = int(input("Digite um número:"))
local=[1,5,8,6,4,2,5,1,3,6,0,8,5,4,6,9,7,9,8,6,3,2,5,4,7,1,0,3,2,1,5,6,8,4,9,7,0,3,2,5,5,1,2,6,5,2,2,0,5,2,6,5,1,5,5,4]
print(ocorrencias(oco,local))

