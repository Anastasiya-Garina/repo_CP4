a = int(input("Введите размерность массива A: "))
massiv_a = []
for i in range(a):
    n = input("Введите элемент: ", )
    massiv_a.append(n)
print(massiv_a)

b = int(input("Введите размерность массива B: "))
massiv_b = []
for i in range(b):
    n = input("Введите элемент: ", )
    massiv_b.append(n)
print(massiv_b)

massiv = sorted(massiv_a + massiv_b)
mas_povtor = []
for i in range(len(massiv)):
    if massiv[i] == massiv[i-1]:
        mas_povtor.append(massiv[i])
    i += 1
print(massiv)
print(set(mas_povtor))