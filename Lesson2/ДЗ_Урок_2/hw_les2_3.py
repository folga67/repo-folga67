while True:
    userMonth = input('Введите, пожалуйста, номер месяца\n')
    if userMonth.isdigit():
        userMonth = int(userMonth)
        break
    else:
        print("Ошибка. Можно ввести только число")

Month_dict ={1:'Январь',
             2:'Февраль',
             3:'Март',
             4:'Апрель',
             5:'Май',
             6:'Июнь',
             7:'Июль',
             8:'Август',
             9:'Сентябрь',
             10:'Октябрь',
             11:'Ноябрь',
             12:'Декабрь'}
print(Month_dict.get(userMonth))
