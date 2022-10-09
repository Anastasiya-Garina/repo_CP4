a = int(input("Введите размерность массива: "))
massiv = []
for i in range(a):
    chiclo = float(input("Введите число: ", ))
    massiv.append(chiclo)
#print(massiv)

maxim = max(massiv)
ind = massiv.index(maxim)
#print(maxim, ind)

for i in range(ind+1, a):
    massiv[i] = 0
    i += 1
print(massiv)