# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.

from fractions import Fraction

# data_1, data_2 = input('Введите первую дробь: '), input('Введите вторую дробь: ')

# data_1 = '2/3'
# data_2 = '5/18'

# data_1 = '0/2'
# data_2 = '1/2'

data_1 = '1/2'
data_2 = '1/2'

# преобразовываем данные в список
data_1 = data_1.split('/')  # числитель и знаменатель 1 дроби
data_2 = data_2.split('/')  # числитель и знаменатель 2 дроби

# приводим к общему знаменателю для операции суммирования дробей
data_1_num = int(data_1[0]) * int(data_2[1])  # числитель 1-ой дроби
data_2_num = int(data_2[0]) * int(data_1[1])  # числитель 2-ой дроби
denum = int(data_2[1]) * int(data_1[1])  # общий знаменатель для суммирования
denum1 = denum  # просто перемножаем
# возвращаем сумму и произведение дробей
sum_num = data_1_num + data_2_num  # сумма числителей
multi_num = int(data_1[0]) * int(data_2[0])  # произведение числителей


# вычисляем НОД и делим числитель и знаменатель на НОД
def to_simple_fraction(x, y):
    while True:
        gcd = 1
        for i in range(2, min(x, y)+1):
            if x % i == 0 and y % i == 0:
                gcd = i
        if gcd == 1:
            break
        x //= gcd
        y //= gcd

    if x == y:
        return '1'
    elif x == 0:
        return '0'
    else:
        return f'{x}/{y}'


print(f'Сумма дробей: {to_simple_fraction(sum_num, denum)}')
print(f'Произведение дробей: {to_simple_fraction(multi_num, denum1)}')

# делаем проверки модулем fractions
a, b = Fraction(int(data_1[0]), int(data_1[1])), Fraction(int(data_2[0]), int(data_2[1]))
print(f'Проверка суммы дробей: {a + b}')
print(f'Проверка произведения дробей: {a * b}')
