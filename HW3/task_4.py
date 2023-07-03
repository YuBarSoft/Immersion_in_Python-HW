# Задача 4. Создайте словарь со списком вещей для похода в качестве ключа и их массой в качестве значения.
# Определите какие вещи влезут в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

items = {
    "спальный мешок": 2,
    "палатка": 7,
    "топор": 2,
    "посуда": 8,
    "еда": 15,
    "одежда": 12,
    "вода": 10
}

max_weight = 30
sum_weight = 0
bag = {}

for item, weight in items.items():
    if sum_weight + weight <= max_weight:
        bag[item] = weight
        sum_weight += weight

print(f'В рюкзаке вместительностью {max_weight} кг могут поместиться:')
for item, weight in bag.items():
    print(f'\t{item} ({weight} кг)')

