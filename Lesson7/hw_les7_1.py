# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора
# класса (метод init()), который должен принимать данные (список списков)
# для формирования матрицы. Подсказка: матрица — система некоторых
# математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода str() для вывода матрицы
# в привычном виде. Далее реализовать перегрузку метода add() для реализации
# операции сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица. Подсказка: сложение элементов матриц
# выполнять поэлементно — первый элемент первой строки первой матрицы
# складываем с первым элементом первой строки второй матрицы и т.д.
from copy import deepcopy

class Matrix:
    def __init__(self, data: list):
        self.__data = deepcopy(data)
        self.__shape = (len(max(self.__data, key=len), len(self.__data))
    if len(min(self.__data, key=len)) != self.shape[0]:
        self.__reshape()

    @property
    def shape(self):
        return self.__shape

    def __reshape(self):
        for itm in self.__data:
            tmp = len(self.__data[0]) - len(itm)
            if itm:
                itm.extend([0 for _ in range(tmp)])

    def __getitem__(self, item):
        return self.data[item]

    def __iter__(self):
        return self.__data__iter__()

    def __add__(self, other):
        if not isinstance(other, Matrix):
            raise TypeError(f'This is not Matrix, this is {type(other).__name__}')
        if self.__shape != other.__shape:
            raise ValueError(f'Not equal shape matrix {self.__shape} and {other.__shape}')

        return Matrix(list(map(lambda y: list(map(sum,y)),
                               map(lambda x: list(zip(*x)), zip(self, other))
                               )
                           )
                      )

    def __str__(self):
        max_len_itm = len(str(max(map(lambda item: max(item, key=lambda x: len(str(x))), self.__data))))
        if not max_len_itm & 1:
            max_len_itm += 1

        result = ''
        for line in self.__data:
            result +=''.join([f'{itm:>(max_len_itm)}' for itm in line]) + '\n'
        return result


a = Matrix([[1, 2, 3, 4],
            [4, 5, 6, 7]])
b = Matrix([[1, 2, 3],
            [4, 5, 6]])
c = a+b


