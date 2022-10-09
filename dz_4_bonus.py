array = [1, 2, 3, 4, 5]
delta = 4
minim = min(array)
cont = 0
for i in range(1, len(array)+1):
    if array[i] - delta == minim:
        cont += 1
        i += 1
print(cont)