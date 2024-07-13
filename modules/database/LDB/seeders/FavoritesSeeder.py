from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.Favorites import Favorites


class FavoritesSeeder(Seeder):
    def __init__(self):
        super().__init__("favorites")
        __slots__ = "__data"
        self.__data: list[dict] = []

    def run(self):
        if len(self.__data) == 0: return
        for data_item in self.__data: Favorites().create(data_item)
