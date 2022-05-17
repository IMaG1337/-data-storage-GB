"""
Каждое из слов «разработка», «сокет», «декоратор» представить в строковом формате и
проверить тип и содержание соответствующих переменных. Затем с помощью
онлайн-конвертера преобразовать строковые представление в формат Unicode и также
проверить тип и содержимое переменных.
"""

WORD_1 = 'разработка'
WORD_2 = 'сокет'
WORD_3 = 'декоратор'
words = [WORD_1, WORD_2, WORD_3]

for word in words:
    print(word, type(word))

print("***************")
WORD_1_UNICODE = '\u0440\u0430\u0437\u0440\u0430\u0431\u043e\u0442\u043a\u0430'
WORD_2_UNICODE = '\u0441\u043e\u043a\u0435\u0442'
WORD_3_UNICODE = '\u0434\u0435\u043a\u043e\u0440\u0430\u0442\u043e\u0440'

words_unicode = [WORD_1_UNICODE, WORD_2_UNICODE, WORD_3_UNICODE]
for word in words_unicode:
    print(word, type(word))
