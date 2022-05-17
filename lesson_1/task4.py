"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из
строкового представления в байтовое и выполнить обратное преобразование (используя
методы encode и decode).
"""

word_1 = 'разработка'
word_2 = 'администрирование'
word_3 = 'protocol'
word_4 = 'standard'

words = [word_1, word_2, word_3, word_4]
words_bites = []
for word in words:
    words_bites.append(word.encode('utf-8'))

words_str = []
for word in words_bites:
    words_str.append(word.decode('utf-8'))

print(words_str)
print(words_bites)
