from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.News import News


class NewsSeeder(Seeder):
    def __init__(self):
        super().__init__("news")
        __slots__ = "__data"
        self.__data: list[dict] = []

    def run(self):
        if len(self.__data) == 0: return
        for data_item in self.__data: News().create(data_item)
