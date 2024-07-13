from modules.database.LDB.system.Migration import Migration

class News(Migration):
    def __init__(self):
        super().__init__("news")
        __slots__ = "__columns"
        self.__columns: dict[str, str] = {
            "id": "int|unique|const|auto",
            "created_at": "str|datetime|const|auto",
            "updated_at": "str|datetime|auto",
        }

    def up(self): super().migration(self.__columns)

    def drop(self): super().drop()

    def fresh(self):
        self.drop()
        self.up()
