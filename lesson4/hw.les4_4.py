a = input("Введите перечень чисел").split()
for i, itm in enumerate(a):
    a[i] = int(itm)
b = [itm for itm in a if a.count(itm) == 1]
print(b)