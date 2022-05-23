"""
a. Подготовить данные для записи в виде словаря, в котором первому ключу
соответствует список, второму — целое число, третьему — вложенный словарь, где
значение каждого ключа — это целое число с юникод-символом, отсутствующим в
кодировке ASCII (например, €);

b. Реализовать сохранение данных в файл формата YAML — например, в файл file.yaml.
При этом обеспечить стилизацию файла с помощью параметра default_flow_style, а
также установить возможность работы с юникодом: allow_unicode = True;

c. Реализовать считывание данных из созданного файла и проверить, совпадают ли они
с исходными.
"""
import yaml

dict = {
    "items": ["computer", "printer", "keyboard", "mouse"],
    "items_quantity": 4,
    "items_ptice": {
        "computer": "200€-1000€",
        "keyboard": "5€-50€",
        "mouse": "4€-7€",
        "printer": "100€-300€",
    },
}

with open("file.yaml", "w") as file:
    yaml.dump(dict, file, default_flow_style=False, allow_unicode=True)

with open("file.yaml", "r") as file:
    file_read = yaml.load(file)
    if file_read == dict:
        print("Данные совпадают")
    else:
        print("Данные не совпадают")
