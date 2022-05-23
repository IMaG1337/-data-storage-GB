"""
a. Создать функцию write_order_to_json(), в которую передается 5 параметров — товар
(item), количество (quantity), цена (price), покупатель (buyer), дата (date). Функция
должна предусматривать запись данных в виде словаря в файл orders.json. При
записи данных указать величину отступа в 4 пробельных символа;

b. Проверить работу программы через вызов функции write_order_to_json() с передачей
в нее значений каждого параметра.
"""
import json


def write_order_to_json(item, quantity, price, buyer, date):
    data = {}
    with open("orders.json", "r") as file:
        data = json.load(file)
    data["orders"].append(
        {
            "item": item,
            "quantity": quantity,
            "price": price,
            "buyer": buyer,
            "date": date,
        }
    )
    with open("orders.json", "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)


write_order_to_json("принтер", "10", "6700", "Ivanov I.I.", "24.09.2017")
write_order_to_json("scaner", "20", "10000", "Petrov P.P.", "11.01.2018")
