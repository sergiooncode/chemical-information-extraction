from abc import ABC
from abc import abstractmethod


# TODO: implememnts message
class Command(ABC):
    _MESSAGE_TYPE = "command"

    @abstractmethod
    def success_message(self):
        pass

    def message_type(self):
        return self._MESSAGE_TYPE
