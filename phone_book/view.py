
commands = ['Открыть файл',
            'Сохранить файл',
            'Показать все контакты',
            'Создать контат',
            'Удалить контакт',
            'Изменить контакт',
            'Найти контакт',
            'Выход из программы']

def main_menu():
    print('Главное меню:')
    for i, item in enumerate(commands, 1):
        print(f'\t{i}. {item}')

    while True:
        try:
            choice = int(input('Выберите пункт меню: '))
            if  0 < choice < 9:
                return choice
            else:
                print('Введите значение от 1 до 8: ')
        except ValueError:
            print('Введите корректное значение: ')  
      


def show_contacts(phone_list: list):
    if len(phone_list) < 1:
        print('Телефонная книга пуста или не открыта')
    else:
        print()
        for i, contact in enumerate(phone_list, 1):
            print(f'\t{i}. {contact[0]:30} {contact[1]:13} {contact[2]:20}')
        print()

'''def input_error():
    print()
    print('Ошибка ввода. Введите корректный пункт меню: ')
    print()'''

def empty_request():
    print('Искомый контакт не найден!')

def many_request():
    print('Уточните данные. Найдено более одного контакта.')

def end_programm():
    print('Всего доброго. Программа завершена')

def create_new_contact():
    name = input('Введите ФИО: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def find_contact():
    find = input('Введите искомый элемент: ')
    return find

def select_contact(message: str):
    contact = input(message)
    return contact

def change_contact():
    print('Введите новые данные (если изменения не требуются, нажмите "Enter")')
    name = input('Введите ФИО: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return name, phone, comment

def delete_confirm(contact: str):
    result = input(f'Вы действительно хотите удалить контакт {contact}? (Y/N): ').lower()
    if result == 'y':
        return True
    else:
        return False
    
def information(message):
    print(message)