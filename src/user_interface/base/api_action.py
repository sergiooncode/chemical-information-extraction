import sys
import traceback

from flask import request as flask_request

from src.application.service.application_service import ApplicationService
from src.user_interface.action.action_interface import ActionInterface
from src.user_interface.http.server_request import ServerRequest

from src.common.logging.base.logging_interface import LoggerInterface


class ApiAction(ActionInterface):
    def __init__(self, logger: LoggerInterface = None, service: ApplicationService = None):
        self._logger = logger
        self._service = service

    def handle(self):
        try:
            return self.execution()

        except Exception as e:
            traceback.print_exc()
            server_request = self._get_server_request()
            self._handle_error(server_request, str(e))
            return {
                "status": {"text": "Internal Server Error"},
            }, 500

    def execution(self):
        pass

    def _log_error(self, exception, request, message=None):
        self._logger.error(self._error_message(exception, request, message))

    def _get_server_request(self) -> ServerRequest:
        return ServerRequest(flask_request)

    def _error_message(self, exception, request: ServerRequest, message=None) -> dict:
        return {
            "exception": {
                "message": exception["trace"],
                "file": exception["filename"],
                "line": exception["line"],
                "name": exception["type"],
            },
            "request": {
                "body": request.parsed_body(),
                "query": request.query_params(),
            },
            "message": message,
        }

    def _handle_error(self, request, message=None):
        trace = traceback.format_exc()
        exc_type, exc_value, exc_traceback = sys.exc_info()
        self._log_error(
            {
                "trace": trace,
                "line": exc_traceback.tb_lineno,
                "filename": exc_traceback.tb_frame.f_code.co_filename,
                "type": exc_type.__name__,
            },
            request,
            message,
        )
