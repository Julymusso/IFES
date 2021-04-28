def Binario_Decimal():
	Caracter_Binario = input('Digite o número binário que deseja converter para decimal: \n')
	CB = Caracter_Binario

	CB0=(2**7)*(int(CB[slice(0,1,1)]))
	CB1=(2**6)*(int(CB[slice(1,2,1)]))
	CB2=(2**5)*(int(CB[slice(2,3,1)]))
	CB3=(2**4)*(int(CB[slice(3,4,1)]))
	CB4=(2**3)*(int(CB[slice(4,5,1)]))
	CB5=(2**2)*(int(CB[slice(5,6,1)]))
	CB6=(2**1)*(int(CB[slice(6,7,1)]))
	CB7=(2**0)*(int(CB[slice(7,8,1)]))
	
	Numero_Decimal = CB0+CB1+CB2+CB3+CB4+CB5+CB6+CB7
	print ('O numero decimal é: \n',Numero_Decimal)

def Decimal_Binario():
	Caracter_Decimal = input ('Digite o número decimal que deseja converter para binário: \n')
	CD = int(Caracter_Decimal)
	
	CD0=CD%2
	CD=CD//2
	
	CD1=CD%2
	CD=CD//2
	
	CD2=CD%2
	CD=CD//2
	
	CD3=CD%2
	CD=CD//2
	
	CD4=CD%2
	CD=CD//2
	
	CD5=CD%2
	CD=CD//2
	
	CD6=CD%2
	CD=CD//2
	
	CD7=CD%2
	
	Numero_Binario = str(CD7)+str(CD6)+str(CD5)+str(CD4)+str(CD3)+str(CD2)+str(CD1)+str(CD0)
	
	print ('O número binário é: \n',Numero_Binario)
