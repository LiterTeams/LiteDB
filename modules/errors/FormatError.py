class FormatError(Exception):
    def __init__(self, message: str = "File Format Error"):
        self.message = message
        super().__init__(self.message)
