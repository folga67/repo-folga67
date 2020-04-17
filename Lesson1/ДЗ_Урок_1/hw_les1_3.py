while True:
    n = input("Введите, пожалуйста, целое число\n")
    if n.isdigit():
        break
    else:
        print("Ошибка. Надо ввести целое число")

number1 = int(n)
number2 = int(n+n)
number3 = int(n+n+n)

sum = number1+number2+number3
print(sum)

