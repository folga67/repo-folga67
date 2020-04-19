a = float(input("Введите аргумент 1\n"))

while True:
    b = float(input("Введите аргумент 2\n"))
    if b == 0:
         print("Делить на 0 нельзя")
    else:
        break

def my_func():
    result = a / b
    return result
print(my_func())