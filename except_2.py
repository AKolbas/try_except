documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': []
}

def check():
    for doc in documents:
        try:
            print(doc['name'])
        except KeyError:
            print(f' У документа с номером {doc["number"]} НЕТ ПОЛЯ NAME')


def people(numbers):
    for doc in documents:
        if doc['number'] == numbers:
            print(doc['name'])
            break
    else:
        print('Такого номера не существует, проверьте данные!')


def list_people():
    for all_info in documents:
        print(all_info['type'], all_info['number'], all_info['name'])

def shelf_dir(numbers):
    # input_num = input('Введите номер документа: ')
    for shelf_num in directories.items():
        for doc_num in shelf_num[1]:
            if doc_num == numbers:
                print('Документ на полке: ', doc_num[0])
                break
        if doc_num == numbers:
            break
    else:
        print('Такого документа не существует!')


def add_doc(new_type, new_number, new_name, new_shelf):
    if int(new_shelf) == 1 or int(new_shelf) == 2 or int(new_shelf) == 3:
        documents.append({"type": new_type, "number": new_number, "name": new_name})
        directories[new_shelf].append(new_shelf)
    else:
        print('Такой полки не существует!')


def main():
    while True:
        print(
            '\n Добро пожаловать в электронный справочник! \n Для работы выберите: \n p – команда, которая выведет имя человека, по номеру документа \n l – команда, которая выведет список всех документов \n s – команда, которая спросит номер документа и выведет номер полки, на которой он находится \n '
            'a – команда, которая добавит новый документ в каталог \n q - команда для выхода из программы \n c - команда выведет все имена и проверит наличие поля "name" \n')
        user_input = input('Введите команду: ')
        if user_input == 'p':
            people(input('Введите номер документа: '))
            break
        elif user_input == 'l':
            list_people()
            break
        elif user_input == 's':
            shelf_dir(input('\n Введите номер документа: '))
            break
        elif user_input == 'a':
            add_doc(input('\n Введите тип документа: '), input('\n Введите номер документа: '),
                    input('\n Введите имя и фамилию: '), input('\n Введите номер полки хранения: '))
            break
        elif user_input == 'c':
            check()
            break
        elif user_input == 'q':
            print('До свидания!')
            break
        else:
            print('Вы ввели неверную информацию! ')

main()




