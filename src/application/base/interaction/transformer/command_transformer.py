from abc import abstractmethod

from src.application.base.interaction.command.command import Command
from src.application.base.interaction.transformer.transformer import Transformer
from src.user_interface.base.http.server_request_interface import ServerRequestInterface


class CommandTransformer(Transformer):
    def __init__(
        self,
        request: ServerRequestInterface,
    ):
        self._request = request

    def transforms_to(
        self,
    ):
        return self.__class__.__name__

    @abstractmethod
    def transform_request(
        self,
        request: ServerRequestInterface,
    ) -> Command:
        pass
