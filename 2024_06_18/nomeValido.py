

def validacao(nome: str | None = None) -> str | None:
	if nome == "":
		return None
		
	quantidade_de_palavras = nome.split(" ")
	if len(quantidade_de_palavras) >= 1:
		nomes = []
		for palavra in quantidade_de_palavras:
			nomes.append(palavra.capitalize())
			
		nomes = str(nomes)
		return nomes
		
	else:
		return "False"


valid_name = "False"
while valid_name == "False":
	nome = input("Digite um nome\n")
	valid_name = validacao(nome)
	
print(valid_name)
