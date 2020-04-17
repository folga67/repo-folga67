while True:
    Rev = input("Укажите, пожалуйста, объем выручки Вашей фирмы за период в рублях\n")
    if Rev.isdigit():
        Rev = int(Rev)
        break
    else:
        print("Ошибка. Надо ввести положительное число")

Cost = input("Укажите, пожалуста, сумму издержек Вашей фирмы за аналогичный период в рублях\n")
while True:
    if Cost.isdigit():
        Cost = int(Cost)
        break
    else:
        print("Ошибка. Надо ввести положительное число")

Profit = Rev - Cost
Pro = Profit / Rev * 100

if Profit > 0:
    print('Ваша фирма за период получила {0} рублей прибыли, рентабельность составила {1:.2f} %.'.format(Profit, Pro))

    ftp = input("Укажите количество сотрудников, работающих на Вашей фирме\n")
    while True:
        if ftp.isdigit():
            ftp = int(ftp)
            break
        else:
            print("Ошибка. Надо ввести положительное целое число")

    Profit_ftp = Profit / ftp
    print('Прибыль, полученная на одного сотрудника фирмы составляет {0:.2f} рублей.'.format(Profit_ftp))
else:
    print("Ваша фирма ушла в убытки в этом периоде.")



