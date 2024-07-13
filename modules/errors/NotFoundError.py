class NotFoundError(Exception):
    def __init__(self, message: str):
        self.__status = "Code Status: 404"
        self.message = f"{self.__status} | {message}"
        super().__init__(self.message)
