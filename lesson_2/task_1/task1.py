"""
a. Создать функцию get_data(), в которой в цикле осуществляется перебор файлов с
данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы». Значения
каждого параметра поместить в соответствующий список. Должно получиться четыре
списка — например, os_prod_list, os_name_list, os_code_list, os_type_list. В этой же
функции создать главный список для хранения данных отчета — например, main_data
— и поместить в него названия столбцов отчета в виде списка: «Изготовитель
системы», «Название ОС», «Код продукта», «Тип системы». Значения для этих столбцов также оформить
в виде списка и поместить в файл main_data (также для каждого файла);

b. Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл. В этой
функции реализовать получение данных через вызов функции get_data(), а также
сохранение подготовленных данных в соответствующий CSV-файл;
"""
import csv
import os
import re

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def get_data():
    os_prod_list, os_name_list, os_code_list, os_type_list = [], [], [], []
    main_data = [
        ["Изготовитель системы", "Название ОС", "Код продукта", "Тип системы"]
    ]
    data_dir = os.path.join(BASE_DIR)
    source_files = [i for i in os.listdir(data_dir) if i.split(".")[1] == "txt"]
    for file_name in source_files:
        with open(file_name, "r", encoding="cp1251") as file:
            data = file.read()
            producer = re.search("Изготовитель ОС:\s+(.+)", data).group(1)
            name = re.search("Название ОС:\s+(.+)", data).group(1)
            code = re.search("Код продукта:\s+(.+)", data).group(1)
            type_system = re.search("Тип системы:\s+(.+)", data).group(1)
            os_prod_list.append(producer)
            os_name_list.append(name)
            os_code_list.append(code)
            os_type_list.append(type_system)
    for i in range(len(os_prod_list)):
        main_data.append(
            [
                i + 1,
                os_prod_list[i],
                os_name_list[i],
                os_code_list[i],
                os_type_list[i],
            ]
        )
    return main_data


def write_to_csv():
    with open("data.csv", "w") as file:
        writer = csv.writer(file)
        for line in get_data():
            writer.writerow(line)


write_to_csv()
