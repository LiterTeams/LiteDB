class AlreadyExistsError(Exception):
    def __init__(self, attribute: str, value: str):
        self.message = f"Unable to create {attribute}. The {value} already exists"
        super().__init__(self.message)
