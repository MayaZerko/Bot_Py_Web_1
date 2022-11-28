from abc import abstractmethod, ABC

from src.classes import AddressBook, Record


class UserPreview(ABC):
    @abstractmethod
    def build_preview(self, data: object) -> str:
        pass


class SimplePreview(UserPreview):
    def build_preview(self, data: str) -> str:
        return data


class ContactsPreview(UserPreview):
    def build_preview(self, data: AddressBook) -> str:
        contacts = ''
        page_number = 1

        for page in data.iterator():
            contacts += f'Page №{page_number}\n'

            for record in page:
                contacts += f'{record.get_info()}\n'
                page_number += 1

        return contacts


class ContactPreview(UserPreview):
    def build_preview(self, data: Record) ->str:
        birthday_info = ''
        email_info = ''
        address_info = ''

        phones_info = ', '.join([phone.value for phone in data.phones])

        if data.birthday:
            birthday_info = f' Birthday : {data.birthday.value}'

        if data.email:
            email_info = f' Email : {data.email.value}'

        if data.address:
            address_info = f' Address : {data.address.value}'

        return f'{data.name.value} : {phones_info}{birthday_info}{email_info}{address_info}'


class NotesPreview(UserPreview):
    def build_preview(self, data):
        pass


class NotePreview(UserPreview):
    def build_preview(self, data):
        pass
