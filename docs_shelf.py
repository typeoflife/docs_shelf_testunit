import sys
documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}
docs_now = []

"""p – people"""
def find_people(number_doc):
    for doc in documents:
        if doc["number"] == number_doc:
            return doc["name"]
    else:
        return "Нет такого документа в базе"


"""s – shelf"""
def find_shelf(directs):
    doc_number2 = directs
    for shelf, values in directories.items():
        if doc_number2 in list(values):
            print(f'Номер полки {shelf}')
            return f'Номер полки {shelf}'
    else:
        print('"Нет такого документа в базе"')
        return "Нет такого документа в базе"


"""l– list"""
def show_full_docs():
    for doc_list in documents:
        print()
        for string in doc_list.values():
            docs_now.append(string)
    return docs_now


"""a – add"""
def add_doc(doc_number,doc_type,name_owner,shelf_number):
    new_doc = {}
    doc_number3 = doc_number
    doc_type = doc_type
    name = name_owner
    shelf_number = shelf_number
    for dir in directories.keys():
        if shelf_number in dir:
            directories[shelf_number].append(doc_number3)
            new_doc["type"] = doc_type
            new_doc["number"] = doc_number3
            new_doc["name"] = name
            documents.append(new_doc)
            return "Документ создан"
    else:
        return "Нет полки с таким номером"


"""d – delete"""
def del_doc(doc_number):
    doc_number4 = doc_number
    for doc in documents:
        if doc_number4 in doc["number"]:
            documents.remove(doc)
            for values in directories.values():
                if doc_number4 in list(values):
                    values.remove(doc_number4)
                    return "Документ удален"
            break
    else:
        return "Нет такого документа в базе"


"""m – move"""
def move_doc(doc_number, shelf):
    for shelf_number, values in directories.items():
        if doc_number in list(values):
            values.remove(doc_number)
            directories[shelf].append(doc_number)
            return f"Документ {doc_number} перемещен на полку {shelf}"
    else:
        return "Нет документа в базе"


"""as – add shelf"""
def add_shelf(new_shelf):
    for shelf in directories.keys():
        if shelf == new_shelf:
            print("Такая полка уже есть!")
            return "Такая полка уже есть!"
    else:
        directories[new_shelf] = []
        return f"Полка с номером {new_shelf} создана"


def main(command, number_doc=None, doc_type=None, name=None, shelf=None):
    while True:
        user_command = command
        if user_command == "p":
            return find_people(number_doc)
        elif user_command == "s":
            return find_shelf(number_doc)
        elif user_command == "l":
            return show_full_docs()
        elif user_command == "a":
            return add_doc(number_doc, doc_type, name, shelf)
        elif user_command == "d":
            return del_doc(number_doc)
        elif user_command == "m":
            return move_doc(number_doc, shelf)
        elif user_command == "as":
            return add_shelf(shelf)
        elif user_command == 'q':
            break

