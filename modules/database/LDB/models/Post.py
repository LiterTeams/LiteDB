from modules.database.LDB.system.Model import Model

class Post(Model):
    def __init__(self):
        super().__init__("posts")

    def create(self, data: dict[str, str]) -> None: super().create(data)

    def update(self, obj_id: int, data: object): ...

