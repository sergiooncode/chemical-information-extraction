from abc import ABC
from abc import abstractmethod


class Transformer(ABC):
    @abstractmethod
    def transforms_to(self):
        pass
