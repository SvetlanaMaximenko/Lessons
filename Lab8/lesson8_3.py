#Прочитать сохранённый json-файл и записать данные на диск в csv-файл первой
#строкой которого озаглавив каждый столбец и добавив новый столбец “телефон”.

import csv
import json


with open('data.json', 'r') as file:
    data = file.read()
    json_data = json.loads(data)
    print(json_data)

list_ = list()

with open('users.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    list_ = ["ID", "Name", "Возраст", "Телефон"]
    writer.writerow(list_)
    for key in json_data:
        tel = input(f'Введите телефон {json_data[key][0]} -> ')
        string = str(key) + " " + " ".join(map(str, json_data[key])) + " " + tel
        list_ = list((string.split()))
        writer.writerow(list_)
        
    
 
