def soma_impares_positivo(list):
    contador = 0
    for num in list:                    #para cada numero na lista
        if num % 2 == 1 and num > 0:    #se o numero for impar e positivo
            contador += num             #adiciona o numero ao contador

    if contador in list:                #se o numero está na lista
        return True
    else:                               #senão
        return False

print(soma_impares_positivo([1, 2, 3, 4, 5, 16, -3, 7])) # True
print(soma_impares_positivo([1, 3, 5])) # False
print(soma_impares_positivo([])) # False
print(soma_impares_positivo([2, 3])) # True
