# Прочитайте созданный в прошлом задании csv файл без использования csv.DictReader.
# Распечатайте его как pickle строку.

import pickle

with open('from-pickle-to-csv.csv', 'r', encoding='utf-8') as c:
    csv_string = ''
    for line in c:
        csv_string += line
    pkl = pickle.dumps(csv_string)
    print(pkl)

