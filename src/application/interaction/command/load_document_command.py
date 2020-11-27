from src.application.interaction.command.base_command import BaseCommand


class LoadDocumentCommand(BaseCommand):
    def __init__(self, text: str):
        self.__document_text = text

    @property
    def document_text(self) -> str:
        return self.__document_text
