# Задача 1. Известно, что на доске 8×8 можно расставить 8 ферзей так, чтобы они не били друг друга.
# Вам дана расстановка 8 ферзей на доске, определите, есть ли среди них пара бьющих друг друга.
# Программа получает на вход восемь пар чисел, каждое число от 1 до 8 - координаты 8 ферзей.
# Если ферзи не бьют друг друга верните истину, а если бьют - ложь.
# Используйте генератор случайных чисел для случайной расстановки ферзей в задаче выше.
# Проверяйте различные случайные варианты и выведите 4 успешных расстановки.
# *Выведите все успешные варианты расстановок.

# Ферзи могут бить друг друга в трех случаях:
# на одной горизонтали, на одной вертикали, на одной диагонали.
# Если координаты ферзя обозначить (x,y) тогда получаем условие:
# (x1 == x2)  (y1 == y2)  (abs(x1 - x2) == abs(y1 - y2))

import random

def number_pairs_generator():
    pairs = []
    while len(pairs) < 8:
        pair = (random.randint(1, 8), random.randint(1, 8))
        if pair not in pairs:
            pairs.append(pair)
    return pairs


def search_variable():
    counter_generations = 0
    max_generations = 1000
    good_variable_counter = 0

    while counter_generations < max_generations:
        counter_generations += 1
        print()
        pairs = number_pairs_generator()
        print(f'№ {counter_generations}: {pairs}')

        first_numbers = set(pair[0] for pair in pairs)
        second_numbers = set(pair[1] for pair in pairs)

        if len(first_numbers) != len(pairs):
            print('Ферзи бьются по горизонтали.')
            continue

        elif len(second_numbers) != len(pairs):
            print('Ферзи бьются по вертикали.')
            continue

        elif any(abs(first_numbers[i] - first_numbers[j]) == abs(second_numbers[i] - second_numbers[j]) for i in range(len(pairs)) for j in range(i + 1, len(pairs))):
            print('Ферзи бьются по диагонали.')
            continue

        else:
            print('Ферзи не бьются. Запишем координаты в файл.')
            good_variable_counter += 1
            pairs_str = str(pairs)
            with open('happy-end.txt', 'w+', encoding='utf-8') as file:
                file.write(pairs_str)
            if good_variable_counter == 4:
                break

search_variable()
