numero = int(input("Digite um numero:\n"))

if numero == 0:
	print("1")
	exit()

listaUsuario = [x for x in range(numero + 1)]
booleano = False

while len(listaUsuario) > 1:
	if booleano == False:
		listaUsuario[0] = 1
		booleano = True
	listaUsuario[0] = int(listaUsuario[0]) * int(listaUsuario[1])
	listaUsuario.pop(1)
 
print("Resultado: ", listaUsuario)
exit()