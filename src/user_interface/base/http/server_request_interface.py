class ServerRequestInterface:
    def query_params(
        self,
    ):
        raise NotImplementedError()

    def view_args(
        self,
    ):
        raise NotImplementedError()

    def parsed_body(
        self,
    ):
        raise NotImplementedError()
