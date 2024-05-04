
nasc = input("Digite seu ano de nascimento.\n")
anoAt = 2025 #ano atual
idade = None
        
while (nasc >= "::::::") or (nasc <= "//////"):            #se nao for numero
        nasc = input("Digite apenas um (numero)\n")
#fim while
        
nasc = int(nasc)
        
idade = anoAt - nasc

if (idade > 150) or (idade < 0):
        print("Reprovado")
        exit()
        
est = input("Voce estuda? (1 para SIM ou 2 para NAO)\n")

while (est != "1") and (est != "2"):
        est = input("Digite apenas um resposta (1 para SIM ou 2 para NAO)\n")
#fim while

if (est == "2") and (idade < 14):
        print("Aprovado... Com ressalvas")
        exit()
        
while (est != "1") and (est != "2"):            #se nao for numero
        est = input("Digite apenas um resposta (1 para SIM ou 2 para NAO)\n")
#fim while
        
trab = input("Voce trabalha? (1 para SIM ou 2 para NAO)\n")
        
while (trab != "1") and (trab != "2"):
        trab = input("Digite apenas um resposta\n(1 para SIM ou 2 para NAO)\n")
#fim while

if trab == "1":
        if idade < 14:
                print("Reprovado")
                exit()
        #fim menor trabalhando

        regime = input("Qual seu Regime? Digite apenas o numero da opcao:\n1) MEI\n2) ESTAGIARIO\n3) OUTRO\n")

        while (regime != "1") and (regime != "2") and (regime != "3"):
                regime = input("Digite apenas um resposta\n(1 para MEI ou 2 para ESTAGIARIO ou 3 para OUTRO)\n")
        #fim while

        if (regime == "2") and (est == "2"):
                print("Reprovado")
                exit()
        #fim estagio sem estudo

        sal = input("Qual o seu salario? (numero)\n")

        while (sal >= "::::::") or (sal <= "//////"):
                sal = input("Digite apenas um resposta (numero)\n")
        #fim while

        sal = int(sal)

        if ((regime == "1") and (sal > 6750)) or (sal < 0):
                print("Reprovado")
                exit()
        #se for mei e o salario for maior que 6750

        if (est == "1") and (idade >= 14) and (idade < 16):
                print("Aprovado com resalvas")
                exit()
        #caso ele trabalhe



 
else:
        aposentado = input("Voce e aposentado? (1 para SIM ou 2 para NAO)\n")

        while (aposentado != "1") and (aposentado != "2"):
                aposentado = input("Digite apenas um resposta (1 para SIM ou 2 para NAO)\n")
        #fim while    
        
        if (aposentado == "1") and (idade < 62):
                print("Aprovado... Com resalvas")
                exit()
        #fim if caso esteja aposentado com menos de 62 anos
        
        
print("Aprovado") #Aprova a situacao se n for especificado o problema
exit()  #fim de tudo
