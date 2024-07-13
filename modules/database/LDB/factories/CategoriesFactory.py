from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.models.Categories import Categories

class CategoriesFactory(Factory):
    def __init__(self):
        super().__init__("categories")
        self.__count = 6

    def create(self) -> None: ...
