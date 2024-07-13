from modules.helpers.load_datas import load_datas
from modules.helpers.create_file import create_file
from modules.helpers.text_merge import text_merge

class Seeder:
    def __init__(self, table: str):
        __slots__ = "__table"
        self.__table = table

    def generate(self, table: str | None = None):
        table = table or self.__table
        table_name = table.lower()
        module_name = text_merge(table_name.title())
        class_name = module_name + "Seeder"
        print(f"Seeder Generation: {class_name}...")
        file = load_datas(fn="seeder", ff="txt", path="modules\\database\\LDB\\templates")
        file = file.replace(":moduleName", module_name)
        file = file.replace(":className", class_name)
        file = file.replace(":tableName", table_name if " " not in table_name else table_name.replace(" ", "_"))
        create_file(fn=class_name, ff="py", data=file, folder_name="seeders", rpath="modules\\database\\LDB")
        print(f"Seeder Created: {class_name}")
