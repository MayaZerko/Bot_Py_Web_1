from abc import abstractmethod, ABC




class UserPreview(ABC):
    @abstractmethod
    def build_preview(self, data: object) -> str:
        pass


class SimplePreview(UserPreview):
    def build_preview(self, data: str) -> str:
        return data


class ContactsPreview(UserPreview):
    def build_preview(self, data) -> str:
        contacts = ''
        page_number = 1

        for page in data.iterator():
            contacts += f'Page №{page_number}\n'

            for record in page:
                contacts += f'{record.get_info()}\n'
                page_number += 1

        return contacts


class ContactPreview(UserPreview):
    def build_preview(self, data) ->str:
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
        result = ""
        for note in data.get_notes():
            result += note.get_info()
        return result


class NotePreview(UserPreview):
    def build_preview(self, data):
        result = 20 * "-" + "\n"
        result += f"note id - {data.note_id}\n"
        result += f"note text - {data.note_text}\n"
        if data.note_tags:
            result += f"tags - {' '.join(sorted(tag for tag in data.note_tags))}\n"
        return result
