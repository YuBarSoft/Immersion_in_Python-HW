# Задача 3. В большой текстовой строке подсчитать
# количество встречаемых слов и вернуть 10 самых частых.
# Не учитывать знаки препинания и регистр символов.
# За основу возьмите любую статью из википедии или из документации к языку.

from collections import Counter
import re

with open('article.txt', 'r', encoding='utf-8') as text:
    text = text.read().lower()  # читаем article.txt, переводим все символы в нижний регистр

words = re.findall(r'\b\w+\b', text)  # извлекаем все слова из текста
word_count = Counter(words)  # получаем количество повторов каждого слова
top_words = word_count.most_common(10)  # получаем 10 слов с наибольшим количеством повторений

print('10 самых частых слов из текста:')
for word, count in top_words:
    print(f'\t"{word}": {count}')

