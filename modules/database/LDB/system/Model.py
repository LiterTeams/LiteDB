from modules.database.LDB.system.DB import DB
from modules.helpers.load_datas import load_datas
from modules.helpers.create_file import create_file


class Model(DB):
    def __init__(self, table: str):
        super().__init__(table)
        __slots__ = ("__table", "__connect")
        self.__table = table
        self.__connect = False

    def generate(self, table: str | None = None):
        table = table or self.__table
        file = load_datas(fn="model", ff="txt", path="modules\\database\\LDB\\templates")
        class_name = table.lower().title()
        table_name = table.lower()
        file = file.replace(":className", class_name)
        file = file.replace(":tableName", table_name)
        create_file(fn=class_name, ff="py", data=file, folder_name="models", rpath="modules\\database\\LDB")
        print(f"Model Created: {class_name}")
