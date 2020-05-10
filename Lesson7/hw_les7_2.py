# . Реализовать проект расчета суммарного расхода ткани на производство одежды.
# Основная сущность (класс) этого проекта — одежда, которая может иметь
# определенное название. К типам одежды в этом проекте относятся пальто и костюм.
# У этих типов одежды существуют параметры: размер (для пальто) и рост
# (для костюма). Это могут быть обычные числа: V и H, соответственно.
# Для определения расхода ткани по каждому типу одежды использовать формулы:
# для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
# Проверить работу этих методов на реальных данных.Реализовать общий подсчет
# расхода ткани. Проверить на практике полученные на этом уроке знания:
# реализовать абстрактные классы для основных классов проекта, проверить
# на практике работу декоратора @property.
from abc import ABC, abstractmethod

class Textil(ABC):

    property
    abstractmethod
    def consumption(self):
        pass

    def params(self):
        pass

class Suit(Textil):
    def __init__(self, name, height):
        self.height = height
        self.name = name

    property
    def consumption(self):
        return 2*self.height + 0.3

    property
    def params(self):
        self.height


class Coat(Textil):
    def __init__(self, name, size):
        self.size = size
        self.name = name

    property
    def consumption(self):
       return self.size/6.5 + 0.5

    property
    def params(self):
        self.size

coat = Coat('синее', 4)
suit = Suit('красный', 2)
print(coat.consumption())
print(suit.consumption())
print(coat.consumption()+suit.consumption())