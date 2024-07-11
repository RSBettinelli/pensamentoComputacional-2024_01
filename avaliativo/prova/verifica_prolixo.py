def verifica_prolixo(msg):
    msg = msg.lower()           #deixa toda a string em minusculo
    list_msg = msg.split(" ")   #separa o nome através dos pontos

    dictionary = []             #é uma lista que vou usar para conferir
                                # a posição das palavras para não repetirem

    for word in list_msg:       #adiciona as palavras a lista
        dictionary.append([word])   #coloquei as palavras em listas para juntar com a posição

    for counter in range(len(list_msg)):
        dictionary[counter].append(counter) #para cada palavra adiciona a posição dela

    for word1 in dictionary:
        for word2 in dictionary:        #no segundo for, em algum momento, todas as palavras
                                        #vão se encontrar

            if word1[1] == word2[1]:    #se for a mesma palavra na mesma posição
                continue                #verifica a proxima palavra

            if word1[0] == word2[0]:    #se for a mesma palavra (já foi verificado a posição)
                return word1[0]

    return None     #se não tiver palavras repetidas



msg = 'Estudo Python e estudo IA mas prefiro Python'
print(verifica_prolixo(msg))  # 'estudo'
msg = 'Estudo Python e IA mas prefiro Python'
print(verifica_prolixo(msg))  # 'python'
msg = 'Estudo Python e IA mas prefiro jogar'
print(verifica_prolixo(msg))  # None
msg = 'teste testado de de testar do testado'
print(verifica_prolixo(msg))  # 'testado'
msg = input()
print(verifica_prolixo(msg))  # 'testado'
