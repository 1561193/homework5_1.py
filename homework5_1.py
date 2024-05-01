# Создать новый класс House
# Задать ему новый атрибут numberOfFloors = 10
# В цикле пройтись по атрибуту numberOfFloors и распечатать значение "Текущий этаж равен"
# Полученный код напишите в ответ к домашнему заданию


class House:
    numberOfFloors = 10

    def __init__(self):
        self.numberOfFloors = 10

        for i in range(0, self.numberOfFloors):
            i = i + 1
            print('Текущий этаж равен', i)
         



house = House()
