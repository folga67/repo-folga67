# Реализуйте базовый класс Car. У данного класса должны
# быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать
# текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости. Создайте экземпляры
# классов, передайте значения атрибутов. Выполните доступ к атрибутам,
# выведите результат. Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, speed: int, color: str, name: str, is_police: False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} стартует'

    def stop(self):
        return f'{self.name} остановилась'

    def turn_right(self):
        return f'{self.name} поворачивает направо'

    def turn_left(self):
        return f'{self.name} поворачивает налево'

    def show_speed(self):
        return f'Скорость {self.name} - {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} - {self.speed}')

        if self.speed > 60:
            print('Допустимая скорость превышена')
        else:
            return f'Скорость {self.name} - {self.speed}'


mashina = TownCar(30, 'White', 'машина', False)
print(mashina.show_speed())


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bolid = SportCar(230, 'White', 'болид', False)
print(bolid.show_speed())


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print('Допустимая скорость превышена')
        else:
            print(f'Скорость {self.name} - {self.speed}')

tracktor = WorkCar(500, 'White', 'трактор', False)
print(tracktor.show_speed())

class Police(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

patrul = Police (500, 'White', 'патруль', True)
print(patrul.show_speed())