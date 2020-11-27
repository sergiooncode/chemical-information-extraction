from abc import ABC
from abc import abstractmethod


class LoggerInterface(ABC):
    @abstractmethod
    def critical(self, message):
        pass

    @abstractmethod
    def error(self, message):
        pass

    @abstractmethod
    def warning(self, message):
        pass

    @abstractmethod
    def info(self, message):
        pass

    @abstractmethod
    def debug(self, message):
        pass
