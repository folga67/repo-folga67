n = input("Введите свои имя и Фамилию")
n = n.title()
b = input("Введите свой год рождения")
c = input("Введите город проживания")
c = c.title()
m = input("Введите свой e-mail")
ph = input("Ваш телефон")

def personList(name, birth, city, mail, phone):
    return ' '.join([name, birth, city, mail, phone])
print(personList(name = n, birth = b, city = c, mail = m, phone = ph))