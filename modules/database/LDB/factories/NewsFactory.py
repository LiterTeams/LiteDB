from modules.database.LDB.system.Factory import Factory

class NewsFactory(Factory):
    def __init__(self):
        super().__init__("news")

    def create(self, count: int = 6): super().create(count)
