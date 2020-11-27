from abc import ABC
from abc import abstractmethod


class DocumentDescriptionParser(ABC):
    @abstractmethod
    def parse(self, document_text: str):
        pass
