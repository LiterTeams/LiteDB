from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.models.News import News

class NewsFactory(Factory):
    def __init__(self):
        super().__init__("news")
        self.__count = 6

    def create(self) -> None: ...
