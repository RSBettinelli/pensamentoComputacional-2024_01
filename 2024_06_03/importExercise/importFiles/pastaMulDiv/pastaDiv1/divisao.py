def Div(num1: int, num2: int) -> float:
	#return num1 / num2
	
	
	negativo = False
	if (num1 <= 0):
		negativo = True
		num1 *= (-1)
						# alternativa para not negativo
	if (num2 <= 0):				# if negativo:
		negativo = not negativo		# 	negativo = False
		num2 *= (-1)			# else:
						# 	negativo = True
	
	resultado = 0
	while num1 >= num2:			# se o num2 cabe no num1
		resultado += 1			# aumenta em 1 o resultado
		num1 -= num2			# subtrai o valor de num2 da variavel num1
		
	return contador
	