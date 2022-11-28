from classes import address_book, Record
from decorator import input_error
from sort_files import run_sorting


def get_help():
    instruction = '''
        Start: hello or hi
        Add new contact: add record /name/ /phone phone .../
        Add phone: add phone /name/ /phone/
        Add e-mail: add email /name/ /e-mail/
        Change phone: change phone /name/ /old phone/ /new phone/
        Delete phone: delete phone /name/ /phone/
        Add address: add address /name/ /address/
        Show all contacts: show all
        Search contacts: search /text for search/
        Add birthday to contact: add birthday /name/ /date yyyy-mm-dd/
        Days to next birthday: days to birthday /name/
        Shows contacts that will have birthdays in period: birthdays in range /days/
        Delete contact: delete record /name/
        Sort file in folder: sort folder /path to folder/
        Add note: add note /note text/
        Show all notes: show notes
        Add tags to note: add tags /note id/ /tag tag .../
        Edit note: edit notes /id/ /note text/
        Delete note: delete notes /id/
        Search notes by note text: search notes /text/
        Search notes by tags: search tags /tag tag .../
        Sort notes: sort notes
        Quit: stop, exit, close, good bye
    '''
    return instruction


@input_error
def exit_function():
    """Function for close program"""
    return "good bye"


@input_error
def hello_function():
    return 'How can i help you?'


@input_error
def add_record(data):
    name, *phones = data.split(' ')
    if name in address_book:
        raise ValueError('This contact already exist.')
    record = Record(name)

    for phone in phones:
        record.add_phone(phone)

    address_book.add_record(record)
    return f'You added new contact: {name} with this {phones}.'


@input_error
def add_phone_func(data):
    name, phone = data.split(" ", 1)
    record = address_book[name]
    record.add_phone(phone)
    return 'You added phone'


@input_error
def change_phone(data):
    name, *phones = data.split(' ')
    record = address_book[name]
    record.change_phones(phones)
    return 'You changed phones.'


@input_error
def delete_phone(data):
    name, phone = data.split(' ', 1)

    record = address_book[name]
    if record.delete_phone(phone):
        return f'Phone {phone} for {name} contact deleted.'
    return f'{name} contact does not have this number'


@input_error
def search_function(value):

    records = address_book.search(value)

    search_records = '\n'.join([record.get_info() for record in records])
    return search_records


@input_error
def show_function():
    contacts = ''
    page_number = 1

    for page in address_book.iterator():
        contacts += f'Page №{page_number}\n'

        for record in page:
            contacts += f'{record.get_info()}\n'
            page_number += 1

    return contacts


@input_error
def birthday_func(data):
    name, birthday_date = data.split(" ", 1)
    record = address_book[name]
    record.add_birthday(birthday_date)
    return f"{birthday_date} Дата дня народження створена"


@input_error
def next_birthday_func(name):
    name = name.strip()
    record = address_book[name]
    return f"Святкувати будем через {record.get_days_to_next_birthday()} днів"


@input_error
def search_birthday_func(value):
    records_info = ""
    records = address_book.get_birthdays_in_range(value)

    if not records:
        return 'Відсутні контакти з днем народження в данному діапазоні'

    for record in records:
        records_info += f"{record.get_info()}\n"
    return records_info


@input_error
def address_func(data):
    name, address_date = data.split(" ", 1)
    record = address_book[name]
    record.add_address(address_date)
    return f"{address_date} Тут проживає гарна людина"


@input_error
def email_func(data):
    name, email_date = data.split(" ", 1)
    record = address_book[name]
    record.add_email(email_date)
    return f"{email_date} На цю пошту ми можемо щось надіслати)"


@input_error
def del_record(name):
    address_book.remove_record(name)
    return "You deleted the contact."


def folder_sorting(path_to_folder):
    return run_sorting(path_to_folder)
