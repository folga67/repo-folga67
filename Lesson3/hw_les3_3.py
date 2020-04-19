while True:
    a = input("Введите первое число")
    if a.isdigit():
        a = int(a)
    break
else:
    print("Ошибка. Можно ввести только число")

while True:
    b = input("Введите второе число")
    if b.isdigit():
        b = int(b)
    break
else:
    print("Ошибка. Можно ввести только число")

while True:
    c = input("Введите третье число")
    if c.isdigit():
        c = int(c)
    break
else:
    print("Ошибка. Можно ввести только число")

def my_func(a, b, c):
    if a >= b and b >= c:
        return a + b
    elif a >= c:
        return a + c
    else:
        return b + c
print(my_func(a, b, c))