class HttpRequest:
    def __init__(self, body: dict, param: dict) -> None:
        self.body = body
        self.param = param