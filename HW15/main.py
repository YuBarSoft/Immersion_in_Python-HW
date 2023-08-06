"""
Задача 1. Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.
Соберите информацию о содержимом в виде объектов namedtuple.
Каждый объект хранит
 - имя файла без расширения или название каталога,
 - расширение, если это файл,
 - флаг каталога,
 - название родительского каталога.
В процессе сбора сохраните данные в текстовый файл, используя логирование.
"""

import argparse
import logging
from logger import setup_logger
from directory_info import collect_directory_info

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Collect directory info')
    parser.add_argument('path', type=str, help='Path to the directory')
    args = parser.parse_args()

    setup_logger('logfile.txt')
    result = collect_directory_info(args.path)

    if result:
        for item in result:
            logging.info(f"Name: {item.name}")
            logging.info(f"Extension: {item.extension}")
            logging.info(f"Is Directory: {item.is_directory}")
            logging.info(f"Parent Directory: {item.parent_directory}")
        print("Информация о директории записана в файл.")
    else:
        print("Произошла ошибка. Проверьте путь до директории и данные в лог-файле.")

