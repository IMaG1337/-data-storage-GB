"""
Создать текстовый файл test_file.txt, заполнить его тремя строками: «сетевое
программирование», «сокет», «декоратор». Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""
from chardet.universaldetector import UniversalDetector

detector = UniversalDetector()
with open('test_file.txt', 'rb') as file:
    file_bytes = file.read()
    detector.feed(file_bytes)
detector.close()

with open('test_file.txt', encoding=detector.result['encoding']) as file:
    print(file.read())
