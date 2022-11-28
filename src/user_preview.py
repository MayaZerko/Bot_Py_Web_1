from abc import abstractmethod, ABC

from src.classes import AddressBook


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
    def build_preview(self, data):
        pass


class NotesPreview(UserPreview):
    def build_preview(self, data):
        pass


class NotePreview(UserPreview):
    def build_preview(self, data):
        pass
