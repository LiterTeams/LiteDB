from modules.database.LDB.system.Migration import Migration

class Posts(Migration):
    def __init__(self):
        super().__init__("posts")
        __slots__ = "__columns"
        self.__columns: dict[str, str] = {
            "id": "int|unique|const|auto",
            "user_id": "int|relation:users|const",
            "title": "str|required|minmax[3,64]",
            "image": "str|image|required",
            "created_at": "str|datetime|const|auto",
            "updated_at": "str|datetime|auto",
        }

    def up(self): super().migration(self.__columns)

    def drop(self): super().drop()

    def fresh(self):
        self.drop()
        self.up()
