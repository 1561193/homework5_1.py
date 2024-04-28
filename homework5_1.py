# Создать новый класс House
# Задать ему новый атрибут numberOfFloors = 10
# В цикле пройтись по атрибуту numberOfFloors и распечатать значение "Текущий этаж равен"
# Полученный код напишите в ответ к домашнему заданию


class House:
    numberOfFloors = 10

    def __init__(self):
        self.numberOfFloors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

        for i in range(len(self.numberOfFloors)):
            print('Текущий этаж равен', self.numberOfFloors[i])



house = House()