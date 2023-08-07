import os
import logging
from collections import namedtuple

FileData = namedtuple('FileData', ['name', 'extension', 'is_directory', 'parent_directory'])

def collect_directory_info(path):
    directory_info = []

    try:
        for item in os.listdir(path):
            full_path = os.path.join(path, item)
            name, extension = os.path.splitext(item)
            is_directory = os.path.isdir(full_path)
            parent_directory = os.path.basename(path)

            extension = extension.replace('.', '')

            if is_directory:
                extension = 'None'

            file_data = FileData(name=name, extension=extension, is_directory=is_directory, parent_directory=parent_directory)
            directory_info.append(file_data)

        return directory_info

    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')
        return None
