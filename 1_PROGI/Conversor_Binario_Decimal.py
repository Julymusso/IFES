import Func_Bi_Dec

print('Qual operação deseja realizar?\n','Para converter BINÁRIO para DECIMAL digite 1\n','Para converter DECIMAL para BINÁRIO digite 2\n')

operacao = input()

if operacao == '1':
	Func_Bi_Dec.Binario_Decimal()
	
elif operacao == '2':
	Func_Bi_Dec.Decimal_Binario()
