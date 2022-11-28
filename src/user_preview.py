from abc import abstractmethod


class UserPreview:
    @abstractmethod
    def build_preview(self, data) -> str:
        pass


class SimplePreview(UserPreview):
    def build_preview(self, data):
        pass


class ContactsPreview(UserPreview):
    def build_preview(self, data):
        pass


class ContactPreview(UserPreview):
    def build_preview(self, data):
        pass


class NotesPreview(UserPreview):
    def build_preview(self, data):
        pass


class NotePreview(UserPreview):
    def build_preview(self, data):
        pass
