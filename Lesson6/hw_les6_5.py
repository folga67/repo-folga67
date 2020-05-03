# Реализовать класс Stationery (канцелярская принадлежность).
# Определить в нем атрибут title (название) и метод draw (отрисовка).
# Метод выводит сообщение “Запуск отрисовки.”
# Создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер).
# В каждом из классов реализовать переопределение метода draw.
# Для каждого из классов метод должен выводить уникальное сообщение.
# Создать экземпляры классов и проверить,
# что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__title(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

stationery1 = Stationery()
print(stationery1.draw())

class Pen(Stationery):
    def __init__title(self, title):
        super().__init__(title)

    def draw(self):
        return f'Запуск письма'
pen = Pen()
print(pen.draw())

class Pencil(Stationery):
    def __init__title(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск чертежа'

pencil = Pencil()
print(pencil.draw())

class Handle(Stationery):
    def __init__title(self, title):
        super().__init__(title)

    def draw(self):
        return 'Запуск выделения символа'

handle = Handle()
print(handle.draw())

