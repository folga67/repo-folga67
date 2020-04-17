while True:
    userTime = input("Пожалуйста, введите время в секундах\n")
    if userTime.isdigit():
        userTime = int(userTime)
        break
    else:
        print("Ошибка. Можно ввести только число")

hours = userTime // 3600
minutes = userTime % 3600 // 60
seconds = userTime % 3600 % 60

print('Время {0:02}:{1:02}:{2:02}'.format(hours, minutes, seconds))



