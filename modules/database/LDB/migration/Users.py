from modules.database.LDB.system.Migration import Migration


class Users(Migration):
    def __init__(self):
        super().__init__("users")
        __slots__ = "__columns"
        self.__columns: dict[str, str] = {
            "id": "int|unique|const|auto",
            "nickname": "str|minmax[8,24]",
            "email": "str|email|required|unique",
            "password": "str|minmax[6,36]|hash",
            "role": "str|enum[user,moderator,admin]|default[user]",
            "created_at": "str|datetime|const|auto",
            "updated_at": "str|datetime|auto",
        }

    def up(self): super().migration(self.__columns)

    def drop(self): super().drop()

    def fresh(self):
        self.drop()
        self.up()
