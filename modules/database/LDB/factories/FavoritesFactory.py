from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.models.Favorites import Favorites

class FavoritesFactory(Factory):
    def __init__(self):
        super().__init__("favorites")
        self.__count = 6

    def create(self) -> None: ...
