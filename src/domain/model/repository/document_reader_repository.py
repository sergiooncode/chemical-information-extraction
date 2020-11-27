from abc import ABC
from abc import abstractmethod


class DocumentReaderRepository(ABC):
    @abstractmethod
    def list_by_processed(self, processed_filter: bool):
        pass
