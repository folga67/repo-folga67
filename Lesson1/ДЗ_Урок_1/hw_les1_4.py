while True:
    n = input("Введите, пожалуйста, целое положительное число\n")
    if n.isdigit():
        n = int(n)
        break
    else:
        print("Ошибка. Надо ввести целое положительное число")

m = n % 10
n = n // 10
while n != 0:
    if n % 10 > m:
        m = n % 10
    else:
        n = n // 10
print(m)
