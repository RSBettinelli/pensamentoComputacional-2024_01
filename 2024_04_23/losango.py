numero = int(input("Digite um numero\n"))

if numero % 2 == 0:
	numero += 1

meio = (numero // 2)
asterisco = 1
espaco = meio

if (meio % 2) == 0:
	for n in range(meio):
		if ((n + 1) % 2) == 1:
			print(f"{" " * espaco}#{".#" * (asterisco - 1)}")	
		else:
			print(f"{" " * espaco}#.{"#." * (asterisco - 2)}#")
		
		espaco -= 1
		asterisco += 1
	
	print(f"{"#." * ((meio + 1) // 2)}O{".#" * ((meio + 1) // 2)}")
	
	for n in range(meio):
		espaco += 1
		asterisco -= 1
		if (n % 2) == 1:
			print(f"{" " * espaco}#{".#" * (asterisco - 1)}") 
			
		else:
			print(f"{" " * espaco}#.{"#." * (asterisco - 2)}#")

	
else:
	for n in range(meio):
		if ((n + 1) % 2) == 1:
			print(f"{" " * espaco}#{".#" * (asterisco - 1)}") 

		else:
			print(f"{" " * espaco}#.{"#." * (asterisco - 2)}#")

		espaco -= 1
		asterisco += 1
	
	print(f"#{".#" * (((meio +  1) // 2) - 1)}O{"#." * (((meio + 1) // 2) - 1)}#")
	
	for n in range(meio):
		espaco += 1
		asterisco -= 1
		if ((n + 1) % 2) == 1:
			print(f"{" " * espaco}#{".#" * (asterisco - 1)}") 

		else:
			print(f"{" " * espaco}#.{"#." * (asterisco - 2)}#")


exit()