from modules.database.LDB.system.Model import Model

class News(Model):
    def __init__(self):
        super().__init__("news")

    def create(self, data: dict[str, str]) -> None: super().create(data)

    def update(self, obj_id: int, data: object): ...