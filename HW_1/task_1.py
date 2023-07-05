# 1. Пишем таблицу умножения из семинара.

min_digit = 2
max_digit = 10
tower = 4

for i in range(min_digit, max_digit, tower):
    print()
    for j in range(min_digit, max_digit + 1):
        for t in range(i, i + tower):
            if j == min_digit and t == i + tower - 1:
                print(f'{t:>} x {j:>2} = {t * j:>2}\n', end='')
            elif t == i + tower - 1:
                print(f'{t:>} x {j:>2} = {t * j:>2}\n', end='')
            else:
                print(f'{t:>} x {j:>2} = {t * j:>2}\t\t', end='')

