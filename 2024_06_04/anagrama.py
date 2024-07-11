def anagrama(a: str, b: str) -> bool:
	list1 = compara_str(a)
	sorted(list1)
	list2 = compara_str(b)
	sorted(list2)
		
	if list1 == list2:
		return True
	
	else:
		return False

def compara_str(string):

	list_aux = []
	for char in string:
		list_aux.append(char)
	return list_aux





str1 = input("Digite a primeira palavra SEM espaços\n")
str2 = input("Digite a segunda palavra SEM espaços\n")
print("Anagrama ", anagrama(str1, str2))
