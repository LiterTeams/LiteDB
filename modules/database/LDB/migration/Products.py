from modules.database.LDB.system.Migration import Migration

class Products(Migration):
    def __init__(self):
        super().__init__("products")
        __slots__ = "__columns"
        self.__columns: dict[str, str] = {
            "id": "int|unique|const|auto",
            "catalog_id": "int|required|relation:[Catalogs:id]",
            "category_id": "int|required|relation:[Categories:id]",
            "title": "str|minmax[6,64]",
            "image": "str|required",
            "price": "int|required",
            "discount": "str|minmax[2,4]",
            "created_at": "str|datetime|const|auto",
            "updated_at": "str|datetime|auto",
        }

    def up(self): super().migration(self.__columns)

    def drop(self): super().drop()

    def fresh(self):
        self.drop()
        self.up()
