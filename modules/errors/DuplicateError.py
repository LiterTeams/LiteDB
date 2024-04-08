class DuplicateError(Exception):
    def __init__(self, value, function_name, message="Code Status: 432"):
        self.message = f"{message} | Function: {function_name} | Value: {value}"
        super().__init__(self.message)
