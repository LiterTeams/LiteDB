from modules.helpers.load_datas import load_datas
from modules.helpers.create_file import create_file

class Seeder:
    def __init__(self, table: str):
        __slots__ = "__table"
        self.__table = table

    def generate(self, table: str | None = None):
        table = table or self.__table
        file = load_datas(file_name="seeder", file_format="txt", path="modules\\database\\LDB\\templates")
        module_name = table.lower().title()
        class_name = table.lower().title() + "Seeder"
        table_name = table.lower()
        file = file.replace(":moduleName", module_name)
        file = file.replace(":className", class_name)
        file = file.replace(":tableName", table_name)
        create_file(fn=class_name, ff="py", data=file, folder_name="seeders", rpath="modules\\database\\LDB")
        print(f"Seeder Created: {class_name}")

    def seeder(self): ...
