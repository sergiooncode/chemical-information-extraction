from abc import ABC
from abc import abstractmethod


class DocumentAbstractParser(ABC):
    @abstractmethod
    def parse(self, document_text: str):
        pass
