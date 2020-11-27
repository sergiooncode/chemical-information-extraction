from src.application.base.interaction.command.command import Command
from src.application.base.interaction.transformer.command_transformer import CommandTransformer
from src.application.interaction.command.load_document_command import LoadDocumentCommand


class LoadDocumentCommandTransformer(CommandTransformer):
    def transform_request(
        self,
    ) -> Command:
        return LoadDocumentCommand(text=self._request.parsed_body().get("text"))
