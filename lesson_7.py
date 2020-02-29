with open('car_inf.txt') as f:
    car_inf = []
    for row in f:
        list = [x.strip() for x in row.split(',')]
        car_inf.append(list)

# docx файл
from docxtpl import DocxTemplate

def get_context(Brand, Model, Engine_Volume, Price):
    return {
        'Brand': Brand,
        'Model': Model,
        'Engine_Volume': Engine_Volume,
        'Price': Price
    }

def from_template(Brand, Model, Engine_Volume, Price, template):
    template = DocxTemplate(template)
    data = get_context(Brand, Model, Engine_Volume, Price)
    template.render(data)
    template.save('Auto' + '_car_inf.docx')

def report(Brand, Model, Engine_Volume, Price):
    template = 'car_inf.docx'
    document = from_template(Brand, Model, Engine_Volume, Price, template)

from random import randint
n = randint(0, 4)
car_inf_report = car_inf[n]
report(car_inf_report[0], car_inf_report[1], car_inf_report[2], car_inf_report[3])
# csv файл
import csv

with open('car.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '-')
    writer.writerows(car_inf)

# json файл
import json

with open('car_json.txt', 'w') as f:
    json.dump(str(car_inf), f)
