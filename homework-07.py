"""
Задание 1.

Создать класс TrafficLight (светофор)
и определить у него один приватный атрибут color (цвет) и публичный метод running (запуск).

В рамках метода running реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный)
составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение.
Для имитации "горения" каждого цвета испольщуйте ф-цию sleep модуля time

Переключение между режимами должно осуществляться только
в указанном порядке (красный, желтый, зеленый).

Проверить работу примера, создав экземпляр и вызвав описанный метод.
"""
from time import sleep
from datetime import datetime as dt


class TrafficLight:
    _status = {'красный': 7, 'желтый': 2, 'зеленый': 14}
    _color = ''

    def running(self):
        for color, sw_time in self._status.items():
            self._color = color
            start_new_status = dt.now()

            print(f"Светофор сменил сигнал на '{self._color}' "
                  f"на {sw_time} секунд")

            sleep(sw_time)

            print(f"Мигающий сигнал '{self._color}' после "
                  f"{(dt.now() - start_new_status).seconds} секунд")


if __name__ == '__main__':
    tl = TrafficLight()
    tl.running()

"""
Задание 2.

 
Например: 20м*5000м*25кг*0.05м = 125000 кг = 125 т
"""


class Road:
    _surface_spec_gravity = 0.01

    def __init__(self, length, width):
        self._length = float(length)
        self._width = float(width)

    def asphalt_mass_calculation(self, thickness):
        try:
            return (self._length * self._width
                    * thickness * self._surface_spec_gravity)
        except TypeError:
            return None


if __name__ == '__main__':
    road = Road(1000, 2)
    print(
        'Масса асфальта равна:',
        road.asphalt_mass_calculation(20),
        'тонн'
    )

"""
Задание 3.

Реализовать базовый класс Worker (работник),
в котором определить публичные атрибуты name, surname, position (должность),
и защищенный атрибут income (доход). Последний атрибут должен ссылаться
на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.

Создать класс Position (должность) на базе класса Worker. В классе Position реализовать публичные методы
получения полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).

Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров).

П.С. попытайтесь добить вывода информации о сотруднике также через перегрузку str
str(self) - вызывается функциями str, print и format. Возвращает строковое представление объекта.
"""


class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return sum(self._income.values())


if __name__ == '__main__':
    position_data = [
        {
            'name': 'Иван',
            'surname': 'Петров',
            'position': 'Менеджер',
            'wage': 50000,
            'bonus': 10000
        }

    ]

    for item in position_data:
        position = Position(item)

        print('From data: ', item)
        print('Position name: ', position.name)
        print('Position surname: ', position.surname)
        print('Position full name: ', position.get_full_name())
        print('Position position: ', position.position)
        print('Position total income: ', position.get_total_income())

"""
Задание 4.
Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод init()), 
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц: 3 на 2, 3 на 3, 2 на 4.

31 22
37 43
51 86

3 5 32
2 4 6
-1 64 -8

3 5 8 3
8 3 7 1

Следующий шаг — реализовать перегрузку метода str() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода add() для реализации операции сложения двух объектов класса Matrix (двух матриц). 
Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы складываем с
 первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:
    def __init__(self, data):
        self.data = data

    def __str__(self):
        return '\n'.join(['\t'.join([str(cell) for cell in row]) for row in self.data])

    def __add__(self, other):
        if len(self.data) != len(other.data) or len(self.data[0]) != len(other.data[0]):
            raise ValueError('Матрицы должны быть одинакового размера')

        result = []
        for i in range(len(self.data)):
            row = []
            for j in range(len(self.data[0])):
                row.append(self.data[i][j] + other.data[i][j])
            result.append(row)

        return Matrix(result)


# Пример использования класса
matrix1 = Matrix([[31, 22], [37, 43], [51, 86]])
matrix2 = Matrix([[3, 5, 32], [2, 4, 6], [-1, 64, -8]])

print(matrix1)
# 31 22
# 37 43
# 51 86

print(matrix2)
# 3 5 32
# 2 4 6
# -1 64 -8

matrix3 = matrix1 + matrix2
print(matrix3)
# 34 27 32
# 39 47 12
# 50 150 -8
