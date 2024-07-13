from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.Catalogs import Catalogs


class CatalogsSeeder(Seeder):
    def __init__(self):
        super().__init__("catalogs")
        __slots__ = "__data"
        self.__data: list[dict] = [
            {"catalog": "Electronics"},
            {"catalog": "Software"},
            {"catalog": "Wires"},
            {"catalog": "Tools"},
            {"catalog": "Furniture"},
            {"catalog": "Stationery"},
            {"catalog": "Consumables"},
        ]

    def run(self):
        if len(self.__data) == 0: return
        for data_item in self.__data: Catalogs().create(data_item)
