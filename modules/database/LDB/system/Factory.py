from modules.helpers.create_file import create_file
from modules.helpers.load_datas import load_datas

class Factory:
    def __init__(self, table: str):
        __slots__ = "__table"
        self.__table = table

    def generate(self, table: str | None = None):
        table = table or self.__table
        file = load_datas(file_name="factory", file_format="txt", path="modules\\database\\LDB\\templates")
        # module_name = table.lower().title()
        class_name = table.lower().title() + "Factory"
        table_name = table.lower()
#         file = file.replace(":moduleName", module_name)
        file = file.replace(":className", class_name)
        file = file.replace(":tableName", table_name)
        create_file(fn=class_name, ff="py", data=file, folder_name="factories", rpath="modules\\database\\LDB")
        print(f"Factory Created: {class_name}")


    def create(self, count: int = 6): ...
