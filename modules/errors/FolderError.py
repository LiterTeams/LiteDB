class FolderError(Exception):
    def __init__(self, message: str = "Folder Type Error"):
        self.message = message
        super().__init__(self.message)
