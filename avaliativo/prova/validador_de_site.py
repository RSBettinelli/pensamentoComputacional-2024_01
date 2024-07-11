def valida_trecho(val: str) -> bool:
    # Verifica se val possui tamanho != 0 e todos os caracteres
    # estão dentro de CHAR_VALIDOS
    LETRAS_LOWER = 'abcdefghijklmnopqrstuvwxyz'
    LETRAS_UPPER = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    NUMEROS = '0123456789'
    for c in val:                       #para cada letra
        if not c in LETRAS_LOWER:
            if not c in LETRAS_UPPER:   #compara se a letra está em alguma das constantes
                if not c in NUMEROS:
                    return False        #se não estiver

    return True #se estiver em alguma delas


def verifica_site(site: str) -> bool:
    # Utilize valida_trecho(str) para reduzir código duplicado
    list_site = site.split(".")             #separa o site por pontos

    if len(list_site) <= 1 or len(list_site) > 3:       #se não tiver nenhum ou tiver
        return False                                    # muitos pontos

    if len(list_site) == 2:             #se não começar com o nome
        if list_site[1] != "com" and list_site[1] != "org" and list_site[1] != "net":
            return False                #se o final não for válido

    if len(list_site) == 3:             #se começar com o nome
        if list_site[0] != "www" and list_site[0] != "intra":
            return False                #se o nome não for válido

    if len(list_site) == 3:             #se começar com o nome
        if list_site[2] != "com" and list_site[2] != "org" and list_site[2] != "net":
            return False                #se o final não válido

    if len(list_site) == 2:             #se começar com o nome
        is_valid = valida_trecho(list_site[0])  #verifica se o nome é valido

    if len(list_site) == 3:             #se não começar com o nome
        is_valid = valida_trecho(list_site[1])  #verifica se o nome é valido

    return is_valid         #o começo e o fim estão OK, se o nome também estiver retorna True

print("retorna true para valido e false para invalido")
print(verifica_site('www.teste1.com'))
print(verifica_site('teste2.com'))
print(verifica_site('www.teste3.org'))
print(verifica_site('intra.teste4.net'))
print(verifica_site('teSte5.net'))
print()
print(verifica_site('wWw.teste1.com'))
print(verifica_site('teste2com'))
print(verifica_site('www.teste3.gov'))
print(verifica_site('int.rateste4.net'))
print(verifica_site('intra.teSte5net'))
print(verifica_site('intra.te.Ste5.net'))

inp = input()
print(verifica_site(inp))
