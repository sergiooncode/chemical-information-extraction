from abc import ABC
from abc import abstractmethod


class DocumentTitleParser(ABC):
    @abstractmethod
    def parse(self, document_text: str):
        pass
