# 4. Программа загадывает число от 0 до 1000. Необходимо угадать число за 10 попыток. Программа должна подсказывать
# «больше» или «меньше» после каждой попытки. Для генерации случайного числа используйте код:
# from random import
# num = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint

LOWER_LIMIT = 0
UPPER_LIMIT = 1000
counter_max = 10
counter = 0
num = randint(LOWER_LIMIT, UPPER_LIMIT+1)

print(f'Для тестирования: компьютер загадал число: {num}\n')

for i in range(1, counter_max+1):
    counter += 1
    number = int(input(f'Попытка №{counter} из {counter_max}. Введите число от 0 до 1000: '))
    if number > num:
        print('\tВаше число БОЛЬШЕ загаданного компьютером\n')
    elif number < num:
        print('\tВаше число МЕНЬШЕ загаданного компьютером\n')
    else:
        print(f'''\tВы угадали загаданное компьютером число c {counter} попытки!
        \tПриглашаем Вас на тв-шоу "Битва экстрасенсов"!''')
        break
else:
    print('К сожалению, Вы не смогли угадать число.')
    
