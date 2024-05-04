sideF = int(input("write a front: "))
sideL = int(input("write a side: "))

area = sideF * sideL
perimeter = 2 * (sideF + sideL)
hypotenuse = ((sideF ** 2) + (sideL ** 2)) ** (1/2)

print(f"Area = {area}\nPerimeter = {perimeter}\nHypotenuse = {hypotenuse}")