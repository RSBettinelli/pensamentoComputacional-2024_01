#numerosPrimos_RafaelSB_2024_05_28.py
#say all the PRIME NUMBERS less or equal to a INT

def calculate(num: int):
    for a in range(num + 1):
        continues = False
        if a < 2:
            continues = True

        for b in range(2, round((a / 2) + 1)):
            if a % b == 0:
                continues = True

        if continues is False:
            lista.append(a)

        

test = "a"
_list = []
while not test.isnumeric():
    test = input("\nType a number to see all the previous PRIME NUMBERS\n")
test = int(test)

calculate(test)

print(_list, "\n")