'''
Признаюсь честно: к сожалению, на данный момент не умею так кодить.
Увидел красивое решение у одногруппника https://github.com/proDreams/
Сохранил себе для дальнейшего изучения.


Возьмите задачу о банкомате из семинара 2. Разбейте её на отдельные операции — функции.
Дополнительно сохраняйте все операции поступления и снятия средств в список
Напишите программу банкомат.
Начальная сумма равна нулю.
Допустимые действия: пополнить, снять, выйти.
Сумма пополнения и снятия кратны 50 у.е.
Процент за снятие - 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
После каждой третьей операции пополнения или снятия начисляются проценты - 3%.
Нельзя снять больше, чем на счёте.
При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой операцией, даже ошибочной.
Любое действие выводит сумму денег.
'''

import sys

START_SUM = 0
START_OPERATIONS = 1
RICH_VALUE = 5_000_000
RICH_NALOG = 10
MULT = 50
MAX_NALOG = 600
MIN_NALOG = 30


def check_rich(bal, op, op_list):
    if bal > RICH_VALUE:
        nalog = (bal - RICH_VALUE) // RICH_NALOG
        op_list.append((op, 'Налог на богатство', nalog))
        bal -= nalog
    return bal


def check_input(message):
    while True:
        inp = int(input(message))
        if inp % MULT != 0:
            print("Недопустимая сумма. Сумма должна быть кратна 50!")
        else:
            return inp


def increase(bal, op, op_list):
    inc = check_input("Введите количество для пополнения: ")
    if op % 3 == 0:
        bal += bal * 0.03
    bal += inc
    op_list.append((op, 'пополнение', inc))
    op += 1
    bal = check_rich(bal, op, op_list)
    return bal, op


def decrease(bal, op, op_list):
    bal = check_rich(bal, op, op_list)
    dec = check_input("Введите количество для снятия: ")
    percent = dec * 0.015
    if percent < MIN_NALOG:
        percent = MIN_NALOG
    elif percent > MAX_NALOG:
        percent = MAX_NALOG
    dec_perc = dec + percent
    if bal > dec_perc:
        bal -= dec_perc
    else:
        print("Недостаточно средств!")
    if op % 3 == 0:
        bal += bal * 0.03
    op_list.append((op, 'Снятие', dec))
    op_list.append((op, 'Комиссия за снятие', percent))
    op += 1
    return bal, op


def start():
    balance = START_SUM
    operations = START_OPERATIONS
    operations_list = []
    while True:
        select = int(input(f"""Баланс: {balance}
Операции со счётом: {operations - 1}

Доступные действия:
1. Пополнить
2. Снять
3. Выход

Выберите действие: """))
        match select:
            case 1:
                balance, operations = increase(balance, operations, operations_list)
            case 2:
                balance, operations = decrease(balance, operations, operations_list)
            case 3:
                print('Выполненные операции:', *operations_list, sep="\n")
                sys.exit()
            case _:
                print("Повторите попытку.")


start()
