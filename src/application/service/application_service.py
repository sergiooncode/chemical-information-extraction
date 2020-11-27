from typing import Union

from src.application.base.interaction.query.query import Query

from src.application.base.interaction.command.command import Command


class ApplicationService:
    def execute(self, query_command: Union[Query, Command]):
        pass
