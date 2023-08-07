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

    logger = setup_logger('logfile.txt')
    
    try:
        result = collect_directory_info(args.path)

        if result:
            for item in result:
                logger.info(f"Name: {item.name},"
                             f" Extension: {item.extension},"
                             f" Is Directory: {item.is_directory},"
                             f" Parent Directory: {item.parent_directory}")
            print("Информация о директории записана в файл logfile.txt.")
        else:
            print("Произошла ошибка. Проверьте путь до директории и данные в лог-файле.")

    except Exception as e:
        logging.error(f'Произошла ошибка: {str(e)}')
