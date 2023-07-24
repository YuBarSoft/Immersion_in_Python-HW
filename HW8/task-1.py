# Напишите функцию, которая преобразует pickle файл хранящий список словарей в табличный csv файл.
# Для тестированию возьмите pickle версию файла из предыдущей задачи.
# Функция должна извлекать ключи словаря для заголовков столбца из переданного файла.

import pickle
import csv

pickle_file_path = 'results.pkl'
csv_file_path = 'from-pickle-to-csv.csv'


def convert_pickle_to_csv(pickle_file, csv_file):
    with open(pickle_file_path, 'rb') as file:  # загружаем данные из pickle-файла
        data = pickle.load(file)

    keys = set()  # извлекаем ключи словаря для заголовков столбцов
    for dictionary in data:
        keys.update(dictionary.keys())

    fieldnames = ['path', 'type', 'size', 'parent_directory']  # указываем нужный порядок списка ключей словаря

    with open(csv_file, 'w', newline='', encoding='utf-8') as file:  # записываем данные в csv-файл
        writer = csv.DictWriter(file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(data)


convert_pickle_to_csv(pickle_file_path, csv_file_path)  # вызов функции

