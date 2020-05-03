# Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина). Значения данных атрибутов должны
# передаваться при создании экземпляра класса. Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длинаширинамасса асфальта для покрытия
# одного кв метра дороги асфальтом, толщиной в 1 см*число см толщины полотна.
# Проверить работу метода. Например: 20м*5000м*25кг*5см = 12500 т

class Road:

    def __init__(self, length: float, width: float, asphalt_mass: int):
        self._length = length
        self._width = width
        self.__asphalt_mass = asphalt_mass


    def cover(self, thikness = 1):
        return self._length * self._width * thikness * self.__asphalt_mass

road = Road(20, 30, 25)
print(road.cover())
