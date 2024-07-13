from modules.database.LDB.system.DB import DB
from modules.helpers.load_datas import load_datas
from modules.helpers.write_datas import write_datas
from modules.helpers.find_directory import find_directory
from modules.helpers.create_file import create_file
from modules.helpers.text_merge import text_merge


class Model(DB):
    def __init__(self, table: str):
        super().__init__(table)
        __slots__ = "__table"
        self.__table = table

    def generate(self, table: str | None = None):
        table = table or self.__table
        table_name = table.lower()
        class_name = text_merge(table_name.title())
        print(f"Model Generation: {class_name}...")
        file = load_datas(fn="model", ff="txt", path="modules\\database\\LDB\\templates")
        file = file.replace(":className", class_name)
        file = file.replace(":tableName", table_name if " " not in table_name else table_name.replace(" ", "_"))
        create_file(fn=class_name, ff="py", data=file, folder_name="models", rpath="modules\\database\\LDB")
        print(f"Model Created: {class_name}")
