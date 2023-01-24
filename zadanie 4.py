import json
import openpyxl


with open('file.json') as test:
    file_1 = json.load(test)


book = openpyxl.Workbook()

sheet = book.active
sheet['A1'] = ' '
sheet['B1'] = 'person 1'
sheet['C1'] = 'person 2'
sheet['D1'] = 'person 3'
sheet['E1'] = 'person 4'
sheet['F1'] = 'person 5'
sheet['J1'] = 'person 6'
sheet['A2'] = 'id'
sheet['A3'] = 'name'
sheet['A4'] = 'phone'


book.save('my_book.xlsx')
book.close()
