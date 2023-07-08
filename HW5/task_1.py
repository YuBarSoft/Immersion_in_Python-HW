# Задача №1. Напишите функцию, которая принимает на вход строку — абсолютный путь до файла.
# Функция возвращает кортеж из трёх элементов: путь, имя файла, расширение файла.

path_to_my_file = 'C:\secret-folder\second-folder\my-dir\my-file.jpg'


def make_tuple(path_to_my_file: str) -> tuple():
    lst_path = path_to_my_file.split('\\')
    lst_last_elem = lst_path[-1].split('.')
    path_to_my_file = '\\'.join(lst_path[0:-1])
    filename = lst_last_elem[0]
    filetype = lst_last_elem[1]
    return path_to_my_file, filename, filetype


print(make_tuple(path_to_my_file))
