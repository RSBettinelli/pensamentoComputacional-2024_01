import random

number = random.randint(0, 10)
#number = 6

guess = None
_try = 0

while guess != number:
	_try += 1
	print("The current password is incorrect")
	guess = input("Type the correct password:\n")
	while (guess >= ":") or (guess <= "/////////////////"):			#se nao for numero
		_try += 1
		guess = input("Just numbers\n")

	guess = int(guess)

	while (guess < 0) or (guess > 10):                              #se o numero sair dos limites
		_try += 1
		guess = input("10 is the greatest number and 0 is the smallest")
		
		while (guess >= ":") or (guess <= "/////////////////"):		#se nao for numero
			_try += 1
			guess = input("Just numbers\n")
		
		guess = int(guess)



print(f"Correct password!\nYou have tried {_try} times")