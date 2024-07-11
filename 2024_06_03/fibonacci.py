a = "None"
while not a.isnumeric():
	a = input("Digite um numero inteiro\n")
a = int(a)


list1 = [0, 1]

for x in range(a - 1):
	z = list1[x + 1] + list1[x]
	list1.append(z)

print(list1)
print(list1[a])