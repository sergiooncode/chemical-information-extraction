from flask import Response

from src.application.interaction.transformer.load_document_command_transformer import LoadDocumentCommandTransformer
from src.infrastructure.user_interface import responder
from src.user_interface.base.api_action import ApiAction


class LoadDocumentApiAction(ApiAction):
    def execution(
        self,
    ) -> Response:
        server_request = self._get_server_request()

        command = LoadDocumentCommandTransformer(request=server_request).transform_request()
        self._service.execute(command=command)

        return responder.generate_post()
