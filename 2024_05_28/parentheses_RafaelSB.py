#parenteses_RafaelSB_2024_05_28
#if the "()" is valid = TRUE
#if the "()" isn't valid = FALSE

def parentheses_validator(s: str) -> bool:
    # FALTA preencher
    counter = 0
    for c in s:
        if c == "(":
            counter += 1

        elif c == ")":
            counter -= 1

        if counter < 0:
            return False

    if counter == 0:
        return True
    else:
        return False


# Valores válidos
print(parentheses_validator('()'))
print(parentheses_validator('()()'))
print(parentheses_validator('(())'))
print(parentheses_validator('(()()())'))
print(parentheses_validator('(((())()))'))

# Valores inválidos
print(parentheses_validator(')'))
print(parentheses_validator('('))
print(parentheses_validator('()('))
print(parentheses_validator('()()())'))
print(parentheses_validator('(((())())'))
