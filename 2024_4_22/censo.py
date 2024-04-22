nasc = input("Digite seu ano de nascimento.\n")
anoAt = 2025 #ano atual
idade = None
        
while (nasc >= "AAAAAA"):            #se nao for numero
        nasc = input("Digite apenas um (numero)\n")
#fim while
        
nasc = int(nasc)
        
idade = anoAt - nasc
        
est = input("Voce estuda? (1 para SIM ou 2 para NAO)\n")
        
while (est != "1") and (est != "2")):            #se nao for numero
        est = input("Digite apenas um resposta (1 para SIM ou 2 para NAO)\n")
#fim while
        
trab = input("Voce trabalha? (1 para SIM ou 2 para NAO)\n")
        
while (trab != "1") and (trab != "2"):
        trab = input("Digite apenas um resposta\n(1 para SIM ou 2 para NAO)\n")
#fim while
        
if trab == "1" or "1":
        if idade < 14:
                print("Reprovado")
        #fim menor trabalhando

        regime = input("Qual seu Regime? Digite apenas o numero da opcao:\n1) MEI\n2) ESTAGIARIO\n3) OUTRO\n")

        while (regime != "1") and (regime != "2") and (regime != "3"):
                regime = input("Digite apenas um resposta\n(1 para MEI ou 2 para ESTAGIARIO ou 3 para OUTRO)\n")
        #fim while

        if (regime == 2) and (est == "2"):
                print("Reprovado")
        #fim estagio sem estudo

        sal = input("Qual o seu salario? (numero)\n")

        while (sal >= "AAAAAA"):     $
                sal = input("Digite apenas um resposta (numero)\n")
        #fim while

        sal = int(sal)

        if (regime == 1) and (sal > 6750):
                print("Reprovado")
        #se for mei e o salario for maior que 6750

        aposentado = input("Voce e aposentado? (1 para SIM ou 2 para NAO)\n")

        while (aposentado != "1") and (aposentado != "2"):     $
                aposentado = input("Digite apenas um resposta (1 para SIM ou 2 para NAO)\n")
        #fim while

        if (aposentado == 1) and (idade < 62):
                print("Aprovado... Com resalvas")
        #caso esteja aposentado com menos de 62 anos

        if (trab == 1) and (idade >= 14) and (idade < 16):
                print(aprovado com resalvas")

renda = None


