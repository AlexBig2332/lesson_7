with open('car_inf.txt') as f:
    lists = (f.read())
    car_inf = list(lists.split(','))

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
    template.save('Win' + '_car_inf.docx')

def report(Brand, Model, Engine_Volume, Price):
    template = 'car_inf.docx'
    document = from_template(Brand, Model, Engine_Volume, Price, template)

report(car_inf[0], car_inf[1], car_inf[2], car_inf[3])

# csv файл
import csv

with open('car.csv', 'w') as file:
    writer = csv.writer(file, delimiter = '-')
    writer.writerow(car_inf)

# json файл
import json

with open('car_json.txt', 'w') as file:
    json.dump(car_inf, file)
