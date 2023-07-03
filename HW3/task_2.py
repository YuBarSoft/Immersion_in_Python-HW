# Задача 2. Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

import random

numbers = list(range(1, 101))  # создаем список чисел от 1 до 100
lst = []
for i in range(10):
    num = random.choice(numbers)  # выбираем случайное число из списка
    count = random.randint(2, 3)  # генерируем случайное количество повторений (2 или 3)
    lst.extend([num] * count)  # добавляем число в список lst нужное количество раз
print(f'Дан список повторяющихся элементов:\n{lst}')

result = []
for number in lst:
    if number not in result:
        result.append(number)
print(f'Cписок с дублирующимися элементами:\n{result}')

