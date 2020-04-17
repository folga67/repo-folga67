while True:
    a = input("Введите результат спортсмена в первый день его тренировок\n")
    if a.isdigit():
        a = int(a)
        break
    else:
        print("Ошибка. Надо ввести положительное число")
while True:
    b = input("Введите результат, которого должен достигнуть спорстмен\n")
    if b.isdigit():
        b = int(b)
        break
    else:
        print("Ошибка. Надо ввести положительное число")

i = 1
while b > a:
   a = a / 100 * 110
   i += 1
else:
    print(i)
