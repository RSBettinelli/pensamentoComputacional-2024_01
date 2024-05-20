import requests

counter = 0
LEN_CEP = 8
cep = ""
past = {}
address = {}

while cep != "0":
	_valid = False
	_num = True
	while _valid is False:
		cep = input("digite o cep a ser verificado:\n")
		for char in cep:
			if not char.isdigit():
				_num = False
		
		if ((len(cep) == LEN_CEP) and (_num == True)) or (cep == "0"):
			_valid = True

	if cep != "0":
		if cep in past:
			print(past[cep])

		else:
			counter += 1
			url = f"https://viacep.com.br/ws/{cep}/json"
			response = requests.get(url).json()
			print(response)
			past[cep] = response

			if response["uf"] in address:
				if response["localidade"] in address[response["uf"]]:
					address[response["uf"]][response["localidade"]].append(response["cep"])
				
				else:
					address[response["uf"]] = {response["localidade"]: [response["cep"]]}
			
			else:
				address[response["uf"]] = {response["localidade"]: [response["cep"]]}	


print(f"\n\nTotal de consultas foi de: {counter}\n")
for key, value in address.items():
	print(f"{key} --> {value}")