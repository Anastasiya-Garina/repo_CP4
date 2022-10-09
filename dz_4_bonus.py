array = [1, 2, 3, 4, 5, 5, 5, 6]
delta = 4
minim = min(array)
cont = 0
for i in range(0, len(array)):
    if int(array[i]) - delta == minim:
        cont += 1
        i += 1
print(cont)