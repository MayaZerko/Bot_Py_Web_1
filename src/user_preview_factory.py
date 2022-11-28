from abc import abstractmethod, ABC

from src.user_preview import UserPreview, SimplePreview, ContactsPreview, ContactPreview, NotesPreview, NotePreview


class AbstractUserPreviewFactory(ABC):
    @abstractmethod
    def create_simple_preview(self) -> UserPreview:
        pass

    @abstractmethod
    def create_contacts_preview(self) -> UserPreview:
        pass

    @abstractmethod
    def create_contact_preview(self) -> UserPreview:
        pass

    @abstractmethod
    def create_notes_preview(self) -> UserPreview:
        pass

    @abstractmethod
    def create_note_preview(self) -> UserPreview:
        pass


class UserPreviewFactory(AbstractUserPreviewFactory):

    def create_simple_preview(self) -> UserPreview:
        return SimplePreview()

    def create_contacts_preview(self) -> UserPreview:
        return ContactsPreview()

    def create_contact_preview(self) -> UserPreview:
        return ContactPreview()

    def create_notes_preview(self) -> UserPreview:
        return NotesPreview()

    def create_note_preview(self) -> UserPreview:
        return NotePreview()
