a = [7, 4, 3, 8, 2]
print(a)
while True:
    userNumber = input('Введите число')
    if userNumber.isdigit():
        userNumber = int(userNumber)
        break
    else:
        print("Ошибка. Можно ввести только число")

for i in range(len(a)):
    if a[i] > userNumber and a[i + 1] < userNumber:
        a.insert(i + 1, userNumber)
        break
    elif a[0] < userNumber:
        a.insert(0, userNumber)
    elif a[-1] > userNumber:
        a.append(userNumber)
print(f'Новый список: {a}')