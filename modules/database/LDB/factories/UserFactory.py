from modules.database.LDB.system.Factory import Factory


class UserFactory(Factory):
    def __init__(self):
        super().__init__("users")
        self.__count = 6

    def create(self) -> None: ...

