from http import HTTPStatus

from flask import Response

from src.infrastructure.user_interface import responder
from src.user_interface.base.api_action import ApiAction


class HealthCheckAction(ApiAction):
    def execution(self) -> Response:
        return responder.generate_get(
            status_code=HTTPStatus.OK,
            message="Chemical Information Extraction - Health Check",
        )
