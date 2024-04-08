from modules.database.LDB.system.Factory import Factory

class UserFactory(Factory):
    def __init__(self):
        super().__init__("users")

    def create(self, count: int = 6): super().create(count)
