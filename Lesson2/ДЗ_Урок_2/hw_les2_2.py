el = list(input('Введите последовательность символов\n'))
for i in range(1, len(el), 2):
    el[i - 1], el[i] = el[i], el[i - 1]
print(''.join([str(i) for i in el]))










