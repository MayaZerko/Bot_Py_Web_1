from abc import abstractmethod

class UserPreviewFactory:
    @abstractmethod
    def create_preview(self) -> object:
        pass

class SimplePreview(UserPreviewFactory):
    def create_preview(self):
        pass

class NotesPreview(UserPreviewFactory):
    def create_preview(self):
        pass

class NotePreview(UserPreviewFactory):
    def create_preview(self):
        pass

class ContactsPreview(UserPreviewFactory):
    def create_preview(self):
        pass

class NotePreview(UserPreviewFactory):
    def create_preview(self):
        pass
