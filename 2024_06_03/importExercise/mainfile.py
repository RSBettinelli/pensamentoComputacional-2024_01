from ImportFiles.pastaMulDiv.pastaDiv1 import divisao
from ImportFiles.pastaMulDiv.pastaMul1 import multiplicacao
from ImportFiles.pastaMulDiv.pastaMul1 import inverteSinal
from ImportFiles.pastaSubAdd.pastaAdd1 import adicao
from ImportFiles.pastaSubAdd.pastaSub1 import subtracao

a = "None"
b = "None"

#while not a.isdigit():
	#a = input("Escolha um numero inteiro\n")

a = input("Escolha um numero inteiro\n")
a = int(a)

#while not b.isdigit():
	#b = input("Escolha outro numero inteiro\n")
b = input("Escolha outro numero inteiro\n")
b = int(b)

print(divisao.Div(multiplicacao.Mul(adicao.Add(a, b), subtracao.Sub(a, b)), 2))

print(f"Add {adicao.Add(a,b)}")
print(f"Sub {subtracao.Sub(a,b)}")
print(f"Mul {multiplicacao.Mul(a,b)}")
print(f"Inv {inverteSinal.Inv(a,b)}")	#pode ser retirado o fator "b" se retirar o num2 da funcao
if b != 0:
	print(f"Div {divisao.Div(a,b)}")
else:
	print("Div None")