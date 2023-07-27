# Напишите функцию, которая получает на вход директорию и рекурсивно обходит её и все вложенные директории.
# Результаты обхода сохраните в файлы json, csv и pickle. Для дочерних объектов указывайте родительскую директорию.
# Для каждого объекта укажите файл это или директория. Для файлов сохраните его размер в байтах, а для директорий
# размер файлов в ней с учётом всех вложенных файлов и директорий. Соберите из созданных на уроке и в рамках
# домашнего задания функций пакет для работы с файлами разных форматов.

import os
import json
import csv
import pickle


def traverse_directory(directory):
    results = []
    total_size = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            size = os.path.getsize(path)
            results.append({
                'path': path,
                'type': 'file',
                'size': size,
                'parent_directory': root
            })
            total_size += size

        dir_size = sum(
            os.path.getsize(os.path.join(root, dir)) for dir in dirs
        )
        results.append({
            'path': root,
            'type': 'directory',
            'size': dir_size,
            'parent_directory': os.path.dirname(root)
        })
        total_size += dir_size

    save_as_json(results)
    save_as_csv(results)
    save_as_pickle(results)
    save_as_abc_csv(results)


def get_dir_size(path):
    total_size = 0
    for root, dirs, files in os.walk(path):
        for file in files:
            file_path = os.path.join(root, file)
            total_size += os.path.getsize(file_path)
    return total_size


def save_as_json(results):
    with open('results.json', 'w') as file:
        json.dump(results, file)


def save_as_csv(results):
    with open('results.csv', 'w', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['path', 'type', 'size', 'parent_directory'])
        for result in results:
            if result['type'] == 'directory':
                dir_size = get_dir_size(result['path'])
            else:
                dir_size = result['size']
            writer.writerow([result['path'], result['type'], dir_size, result['parent_directory']])


def save_as_pickle(results):
    with open('results.pkl', 'wb') as file:
        pickle.dump(results, file)


def save_as_abc_csv(results):
    with open('results.csv', 'r') as file:  # читаем данные из файла result.csv
        reader = csv.reader(file, delimiter=';')
        data = list(reader)

    sorted_data = sorted(data, key=lambda x: x[0])  # сортируем данные по алфавиту в столбце "path"

    with open('result.csv', 'w', newline='') as file:  # Запись отсортированных данных в файл result.csv
        writer = csv.writer(file, delimiter=';')
        writer.writerows(sorted_data)


# Пример использования функции traverse_directory:
directory = 'D:\PLEX'
traverse_directory(directory)

