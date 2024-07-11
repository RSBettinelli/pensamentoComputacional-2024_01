def parcelas_inteiras(valor, parcelas):
    if parcelas > valor or parcelas <= 0:                       #se tiver um numero invalid de
        return None                                             #parcelas

    quantidade_int = int(valor / parcelas)      #valor das parcelas
    lista_parce = []                            #será a saida

    for i in range(parcelas):                   #para cada parcela
        lista_parce.append(quantidade_int)      #adiciona o valor da parcela a lista de saida

    lista_parce[len(lista_parce) - 1] += (valor % parcelas) #se o valor ficar quebrado
                                                        #soma o valor quebrado a ultima parcela


    return lista_parce      #retorna a lista de parcelas



print(parcelas_inteiras(10, 0)) # None
print(parcelas_inteiras(10, 1)) # [10]
print(parcelas_inteiras(10, 2)) # [5, 5]
print(parcelas_inteiras(10, 3)) # [3, 3, 4]
print(parcelas_inteiras(10, 4)) # [2, 2, 2, 4]
print(parcelas_inteiras(10, 5)) # [2, 2, 2, 2, 2]
print(parcelas_inteiras(10, 10)) # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
print(parcelas_inteiras(10, 11)) # None

inp = int(input())
inp2 = int(input())
print(parcelas_inteiras(inp, inp2))
