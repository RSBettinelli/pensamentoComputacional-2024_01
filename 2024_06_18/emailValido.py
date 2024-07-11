
def validacao(email: str = "") -> bool:
	if ".com" in email:
		email_em_lista = email.split(".com")
		if len(email_em_lista) > 2:
			return False
	
		elif "@" in email_em_lista[0]:
			nomes = email_em_lista[0].split("@")
			if len(nomes) > 2:
				return False
			
			for texto in nomes:
				for char in texto:
					if (not char.isalnum()) and char != "_":
						return False
						
			return True
			
		#else: 
		#	return False	
	return False	
	#else:		
	#	return False
	
email = None
while email != "0":
	email = input("digite um email\n")

	if email != "0":
		print(validacao(email))
		
		
print(validacao('') == False)
print(validacao('@') == False)
print(validacao('@@') == False)
print(validacao('abc@@abc.com') == False)
print(validacao('abc@abc.edu') == False)
print(validacao('a_b_c@a_b_c.com.com') == False)

print()

print(validacao('abc@ab-c.com') == True)
print(validacao('a23@123.com') == True)
print(validacao('a_b_c@a_b_c.com') == True)
print(validacao('a_b_c@a_b_c.com') == True)