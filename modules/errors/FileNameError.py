class FileNameError(Exception):
    def __init__(self, message: str = "File Name Error"):
        self.message = message
        super().__init__(self.message)
