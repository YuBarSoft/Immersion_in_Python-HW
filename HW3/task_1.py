# Задача 1. Три друга взяли вещи в поход. Сформируйте словарь, где ключ — имя друга, а значение — кортеж вещей.
# Ответьте на вопросы:
# 1) Какие вещи взяли все три друга
# 2) Какие вещи уникальны, есть только у одного друга и имя этого друга
# 3) Какие вещи есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует
# Для решения используйте операции с множествами.
# Код должен расширяться на любое большее количество друзей.

data = {'Алексей': ('палатка', 'котелок', 'мангал', 'топор', 'веревка'),
        'Константин': ('гитара', 'алкоголь', 'продукты', 'палатка', 'туалетные принадлежности', 'нож'),
        'Анна': ('туалетные принадлежности', 'столовые приборы', 'скатерть', 'походный стол со стульями', 'кастрюля',
                 'сковорода', 'палатка')}

print('1. Какие вещи взяли все три друга?')
# all_frends_values = set.intersection(*map(set, data.values()))  # это вариант про вещи, которые есть у всех друзей
all_items = set()
for items in data.values():
    all_items.update(items)
all_items = list(all_items)
for item in all_items:
    print(f'\t{item}')

print('-------------------------\n2. Какие вещи уникальны (есть только у одного друга)? Укажите имя этого друга.')
lst = []
for frend in data:
    lst.extend(list(data[frend]))
no_item = set()

for frend, value in data.items():
    for i in range(len(value)):
        if lst.count(value[i]) == 1:
            print(f'\t{value[i]} - {frend}')
        if lst.count(value[i]) == len(data) - 1:
            no_item.add(value[i])

print('-------------------------\n3. Какие вещи есть у всех друзей, кроме одного? Укажите имя того, у кого данная вещь отсутствует.')
for frend, value in data.items():
    for i in no_item:
        if i not in data[frend]:
            print(f'\t{i} - {frend}')
