from abc import ABC
from abc import abstractmethod
from typing import Dict
from typing import List
from typing import Union


class DocumentWriterRepository(ABC):
    @abstractmethod
    def add(self, document_details: Dict[str, Union[str, int]]):
        pass

    @abstractmethod
    def update(self, entities: List[str]):
        pass
