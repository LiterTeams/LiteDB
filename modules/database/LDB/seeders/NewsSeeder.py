from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.News import News


class NewsSeeder(Seeder):
    def __init__(self):
        super().__init__("news")
        self.__data: list[dict] = []

    def run(self):
        for data_item in self.__data: News().create(data_item)
