import zipfile

NOME_ARQUIVO = "msg_05_caracteres.zip"
zip_file = zipfile.ZipFile(NOME_ARQUIVO, 'r')


def extrair_arquivo_zip_com_senha(senha):
    try:
        zip_file.extractall(path='.', pwd=senha.encode('utf-8'))
        return True
    except:
        pass
    return False


################################################
# Não alterar linhas acima:
################################################

############################################################################

# para desativar as RESTRICOES COMENTE as linhas:
# 88
# 104
# 140
# 164
# 186
# 209
# 248
# 276

############################################################################

import time


charS = None
caracterAa = None   #se mudarmos as variaveis dos "for" diretamente vai quebrar o ciclo
caracterBa = None
caracterCa = None
caracterSa = None
senha = None
nTentativa = 0

startT = time.time()


# a senha correta e "123"

for size in range(3):
    for caracterA in range(62):        
        if (caracterA >= 0) and (caracterA < 10):
            caracterAa = chr(caracterA + 48)
            
        elif (caracterA >= 10) and (caracterA < 36):
            caracterAa = chr(caracterA + 55)
            
        elif (caracterA >= 36):
            caracterAa = chr(caracterA + 61)
        
		

        for caracterB in range(62):
            if (caracterB >= 0) and (caracterB < 10):
                caracterBa = chr(caracterB + 48)
            
            elif (caracterB >= 10) and (caracterB < 36):
                caracterBa = chr(caracterB + 55)
            
            elif (caracterB >= 36):
                caracterBa = chr(caracterB + 61)
  
			

            for caracterC in range(62):
                if (caracterC >= 0) and (caracterC < 10):
                    caracterCa = chr(caracterC + 48)

                elif (caracterC >= 10) and (caracterC < 36):
                    caracterCa = chr(caracterC + 55)

                elif (caracterC >= 36):
                    caracterCa = chr(caracterC + 61)

                if size == 0:
                    sequencia = 0
                    if (caracterC == caracterB) and (caracterC == caracterA):
                        continue

                    if (int(caracterA < 10)) and (int(caracterB) < 10) and (int(caracterC) < 10):
                        if caracterB == (caracterA + 1):
                            sequencia += 1

                        elif caracterB == (caracterA - 1):
                            sequencia -= 1

                        if caracterC == (caracterB + 1):
                            sequencia += 1

                        elif caracterC == (caracterB - 1):
                            sequencia -= 1
                    
                    if (sequencia >= 2) or (sequencia <= (-2)):
                        continue



                    nTentativa += 1
                    senha = (str(caracterAa) + str(caracterBa) + str(caracterCa))
                    extraido = extrair_arquivo_zip_com_senha(str(senha))
                    if extraido:
                        endT = time.time()
                        print(f"\nArquivo extraido\n{nTentativa} tentativas foram necessarias\n")
                        print(f"{endT - startT} de tempo foi utilizado\nA senha e {senha}")
                        exit()
                    else:
                        print(senha)



                else:
                    for caracterS in range(62):
                        if (caracterS >= 0) and (caracterS < 10):
                            caracterSa = chr(caracterS + 48)

                        elif (caracterS >= 10) and (caracterS < 36):
                            caracterSa = chr(caracterS + 55)

                        elif (caracterS >= 36):
                            caracterSa = chr(caracterS + 61)
                            
                            
                        if size == 1:
                            
                            repetidosA = 0
                            repetidosB = 0
                            repetidosC = 0
                            sequencia = 0
                            if (caracterC == caracterB) and (caracterC == caracterA) and (caracterC == caracterS):
                                continue

                            if caracterB == caracterA:
                                repetidosA += 1
                                repetidosB += 1

                            if caracterC == caracterA:
                                repetidosA += 1
                                repetidosC += 1
                            
                            if caracterC == caracterB:
                                repetidosB += 1
                                repetidosC += 1

                            if caracterS == caracterA:
                                repetidosA += 1
                            
                            if caracterS == caracterB:
                                repetidosB += 1

                            if caracterS == caracterC:
                                repetidosC += 1
                            
                            if (repetidosA >= 2) or (repetidosB >= 2) or (repetidosC >= 2):
                                continue

                            if (int(caracterA) < 10) and (int(caracterB) < 10) and (int(caracterC)  < 10) and (int(caracterS) < 10):
                                if caracterB == (caracterA + 1):
                                    sequencia += 1

                                elif caracterB == (caracterA - 1):
                                    sequencia -= 1

                                if caracterC == (caracterB + 1):
                                    sequencia += 1

                                elif caracterC == (caracterB - 1):
                                    sequencia -= 1
                                
                                if caracterS == (caracterC + 1):
                                    sequencia += 1

                                elif caracterS == (caracterC - 1):
                                    sequencia -= 1
                                    
                            if (sequencia >= 3) or (sequencia <= (-3)):
                                continue

                            nTentativa += 1
                            senha = str(caracterAa) + str(caracterBa) + str(caracterCa) + str(caracterSa)
                            extraido = extrair_arquivo_zip_com_senha(str(senha))
                            if extraido:
                                endT = time.time()
                                print(f"\nArquivo extraido\n{nTentativa} tentativas foram necessarias\n")
                                print(f"{endT - startT} de tempo foi utilizado\nA senha e {senha}")
                                exit()
                            else:
                                print(senha)

                        
                            
                        else:
                            for caracterS2 in range(62):
                                repetidosA = 0
                                repetidosB = 0
                                repetidosC = 0
                                repetidosS = 0
                                sequencia = 0
                                if (caracterC == caracterB) and (caracterC == caracterA) and (caracterC == caracterS) and (caracterC == caracterS2):
                                    continue

                                if caracterB == caracterA:
                                    repetidosA += 1
                                    repetidosB += 1

                                if caracterC == caracterA:
                                    repetidosA += 1
                                    repetidosC += 1
                            
                                if caracterC == caracterB:
                                    repetidosB += 1
                                    repetidosC += 1

                                if caracterS == caracterA:
                                    repetidosA += 1
                                    repetidosS += 1
                            
                                if caracterS == caracterB:
                                    repetidosB += 1
                                    repetidosS += 1

                                if caracterS == caracterC:
                                    repetidosC += 1
                                    repetidosS += 1
                                
                                if caracterS2 == caracterA:
                                    repetidosA += 1
                                
                                if caracterS2 == caracterB:
                                    repetidosB += 1
                                
                                if caracterS2 == caracterC:
                                    repetidosC += 1
                                
                                if caracterS2 == caracterS:
                                    repetidosS += 1
                            
                                if (repetidosA >= 2) or (repetidosB >= 2) or (repetidosC >= 2) or (repetidosS >= 2):
                                    continue

                                if (int(caracterA) < 10) and (int(caracterB) < 10) and (int(caracterC)  < 10) and (int(caracterS) < 10) and (int(caracterS2) < 10):
                                    if caracterB == (caracterA + 1):
                                        sequencia += 1

                                    elif caracterB == (caracterA - 1):
                                        sequencia -= 1

                                    if caracterC == (caracterB + 1):
                                        sequencia += 1

                                    elif caracterC == (caracterB - 1):
                                        sequencia -= 1
                                
                                    if caracterS == (caracterC + 1):
                                        sequencia += 1

                                    elif caracterS == (caracterC - 1):
                                        sequencia -= 1
                                    
                                    if caracterS2 == (caracterS + 1):
                                        sequencia += 1

                                    elif caracterS2 == (caracterS - 1):
                                        sequencia -= 1
                                    
                                if (sequencia >= 4) or (sequencia <= (-4)):
                                    continue

                                if (caracterS2 >= 0) and (caracterS2 < 10):
                                    caracterS2a = chr(caracterS2 + 48)

                                elif (caracterS2 >= 10) and (caracterS2 < 36):
                                    caracterS2a = chr(caracterS2 + 55)

                                elif (caracterS2 >= 36):
                                    caracterS2a = chr(caracterS2 + 61)


                                nTentativa += 1
                                senha = str(caracterAa) + str(caracterBa) + str(caracterCa) + str(caracterSa) + str(caracterS2a)
                                extraido = extrair_arquivo_zip_com_senha(str(senha))
                                if extraido:
                                    endT = time.time()
                                    print(f"\nArquivo extraido\n{nTentativa} tentativas foram necessarias\n")
                                    print(f"{endT - startT} de tempo foi utilizado\nA senha e {senha}")
                                    exit()
                                else:
                                    print(senha)
                            
                            
                    







						