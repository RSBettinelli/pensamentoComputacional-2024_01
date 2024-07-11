def Mul(num1: int, num2: int) -> float:
	#return num1 * num2
	
	negativo = False
	a = num1
	num1 = 0
	if num2 <= 0:
		negativo = True
		num2 *= (-1)
		
	for c in range(num2):
		num1 += a
	
	if negativo:
		num1 *= (-1)
	
	return num1