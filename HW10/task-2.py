# Задача 2. Возьмите любую из задач с прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

import os
from random import randint, uniform
from pathlib import Path


class Fillfile:
    minim = -1000
    maxim = 1000

    def __init__(self, name, quanty, directory):
        self.name = name
        self.quanty = quanty
        self.dir = directory

    def generate(self):
        Path(self.dir).mkdir(parents=True, exist_ok=True)
        path_to_files = Path(self.dir) / self.name
        with open(f'{path_to_files}', 'a+', encoding='utf-8') as f:
            for _ in range(self.quanty):
                print(f'{str(randint(Fillfile.minim, Fillfile.maxim))}|'
                      f'{str(uniform(Fillfile.minim, Fillfile.maxim))}', file=f)


if __name__ == "__main__":
    sample = Fillfile('result.txt', 100, os.getcwd())
    sample.generate()

