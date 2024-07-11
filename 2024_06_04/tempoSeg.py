timeS = "None"
while not timeS.isdigit():
	timeS = input("Digite um tempo em SEGUNDOS\nApenas números INTEIROS\n")
	
timeS = int(timeS)
	
timeM = timeS / 60
timeS = timeS % 60
timeH = timeM / 60
timeM = timeM % 60
timeH = int(timeH)
timeM = int(timeM)

if timeH  >= 1:
	if timeM >= 1:
		if timeS >= 1:
			print(f"Tempo passado:\n{timeH}h : {timeM}min : {timeS}seg")
			
		else:
			print(f"Tempo passado:\n{timeH}h : {timeM}min")
		
	else:
		if timeS >= 1:
			print(f"Tempo passado:\n{timeH}h : 0min : {timeS}seg")
			
		else:
			print(f"Tempo passado:\n{timeH}h")
		
else:
	if timeM >= 1:
		if timeS >= 1:
			print(f"Tempo passado:\n{timeM}min : {timeS}seg")
			
		else:
			print(f"Tempo passado:\n{timeM}min")
		
	else:
		print(f"Tempo passado:\n{timeS}seg")
		
		