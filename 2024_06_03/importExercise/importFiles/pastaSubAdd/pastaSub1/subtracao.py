def Sub(num1: int, num2: int) -> float:
	#return num1 - num2
	
	if num2 <= 0:
		num2 *= (-1)
		for c in range(num2):
			num1 += 1
		
	else:
		for c in range(num2):
			num1 -= 1
		
	return num1