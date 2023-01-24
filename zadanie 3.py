import json

dict_1 = {
    'id': {
        312535: ('Иван', 17),
        583459: ('Александр', 20),
        234678: ('Дмитрий', 20),
        257893: ('Анатолий', 15),
        740134: ('Николай', 19),
        537845: ('Антон', 18)
    }
}

print(type(dict_1))

with open('file.json', 'w') as file:
    json.dump(dict_1, file, indent=3)
