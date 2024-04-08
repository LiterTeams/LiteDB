

class SQLDB:
    def __init__(self):
        self.__status = False

    def start(self, config: object): ...

    def shutdown(self): ...

    @property
    def status(self) -> bool: return self.__status
