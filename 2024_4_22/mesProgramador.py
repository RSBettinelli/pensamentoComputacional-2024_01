import random   #permite usarmos RANDOM

mesDaPessoa = input("Digite seu mes de nascimento.\n")
#pessoa escolhe o mes

while (mesDaPessoa >= "AAAAAA"):            #se nao for numero
	mesDaPessoa = input("Digite apenas um mes (numero) ate 12\n")
#fim while

mesDaPessoa = int(mesDaPessoa)              #string para inteiro

if (mesDaPessoa < 1) or (mesDaPessoa > 12): #se nao for um numero valido
	print("Bota um numero valdio na proxima\nAgora vc tem um mes aleatorio.")
	mesDaPessoa = int(random.randint(1, 12))
#fim mes diferente

if mesDaPessoa == 1:
	print("Python!")
#fim if linguagem 1

elif mesDaPessoa == 2:
        print("Fortan!")
#fim elif linguagem 2 

elif mesDaPessoa == 3:
        print("Rust")
#fim elif linguagem 3

elif mesDaPessoa == 4:
        print("Go!")
#fim elif linguagem 4

elif mesDaPessoa == 5:
        print("Java!")
#fim elif linguagem 5 

elif mesDaPessoa == 6:
        print("JavaScript!")
#fim elif linguagem 6

elif mesDaPessoa == 6:
        print("Linguagem 6")
#fim elif linguagem 6

elif mesDaPessoa == 7:
        print("C!")
#fim elif linguagem 7 

elif mesDaPessoa == 8:
        print("PHP!")
#fim elif linguagem 8 

elif mesDaPessoa == 9:
        print("Haskell!")
#fim elif linguagem 9 

elif mesDaPessoa == 10:
        print("Perl!")
#fim elif linguagem 10 

elif mesDaPessoa == 11:
        print("Swift!")
#fim elif linguagem 11 

elif mesDaPessoa == 12:
        print("Kotlin!")
#fim elif linguagem 12 

else:
	print("Como diabos vc chegou aqui?A")
#fim de tudo, nao deve ser executado pois o numero foi
#aleatorizado entre os possiveis
