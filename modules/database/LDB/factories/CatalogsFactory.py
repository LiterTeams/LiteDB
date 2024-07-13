from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.models.Catalogs import Catalogs

class CatalogsFactory(Factory):
    def __init__(self):
        super().__init__("catalogs")
        __slots__ = "__count"
        self.__count = 6

    def create(self) -> None: ...
