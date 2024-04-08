from modules.database.LDB.system.Factory import Factory

class PostFactory(Factory):
    def __init__(self):
        super().__init__("posts")

    def create(self, count: int = 6): super().create(count)
