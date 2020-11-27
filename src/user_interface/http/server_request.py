from src.user_interface.base.http.server_request_interface import ServerRequestInterface


class ServerRequest(ServerRequestInterface):
    def __init__(self, server_request: object):
        self.__server_request = server_request
        self.__query_params = dict()
        self.__view_args = dict()

    def query_params(self) -> dict:
        return self.__query_params

    def view_args(self) -> dict:
        return self.__view_args

    def parsed_body(self) -> dict:
        return self.__server_request.get_json()

    def __repr__(self):
        return (
            f"<ServerRequest(view_args={self.__view_args}, "
            f"øquery_params={self.__query_params}, "
            f"parsed_body={self.__server_request.get_json()})>"
        )
