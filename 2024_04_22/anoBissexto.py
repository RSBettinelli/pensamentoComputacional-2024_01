ano = input("Digite o ano atual, eu afirmarei se e bissexto\n")

while ano > "AAAAAA":
        ano = input("Digite apenas um ano (numero) de ate 6 digitos\n")
#fim while

ano = int(ano)

if (ano % 4) == 0:
	print("Esse ano e bissexto!")
#fim if divisivel 4

else:
	print("Esse ano não é bissexto.")
	if ((ano + 1) % 4) == 0:
		print(f"O proximo ano sera bissexto. (ano {ano + 1})")
	#fim if (proximo)

	elif ((ano + 2) % 4) == 0:
		print(f"Daqui a 2 anos sera um ano bissexto. (ano {ano + 2})")
	#fim elif 2 anos 

	else:
		print(f"Daqui a 3 anos sera um ano bissexto. (ano {ano + 3})")
	#fim else (3 anos)

#fim else (nao divisivel)
