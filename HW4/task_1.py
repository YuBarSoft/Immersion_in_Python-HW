# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# Напишите функцию, которая при запуске заменяет содержимое переменных, оканчивающихся на s на None (кроме переменной из одной буквы s).
# Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

def replace_variables():
    # создаем переменные
    with_s = "переменная с s в конце"
    second_with_s = "вторая переменная с s в конце"
    without_s_first = "переменная без s в конце"
    without_s_second = "вторая переменная без s в конце"
    s = "тут только буква s"

    local_variables = locals()
    for variable_name, variable_value in local_variables.items():
        if variable_name[-1] == 's' and len(variable_name) > 1:
            variable_name_result = variable_name[:-1]
            print(f"""{variable_name} = None\n{variable_name_result} = '{variable_value}'""")
        else:
            print(f"{variable_name} = '{variable_value}'")


replace_variables()
