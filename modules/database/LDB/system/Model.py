from modules.helpers.find_file import find_file
from modules.helpers.load_datas import load_datas
from modules.helpers.create_file import create_file
from modules.helpers.write_datas import write_datas


class Model:
    def __init__(self, table: str):
        __slots__ = ("__table", "__connect")
        self.__table = table
        self.__connect = False

    def query(self, **params) -> None | object | list:
        r"""
        :param params:
            search: str [optional],
            order_by: asc | desc [optional],
            paginate: int [optional],
        :return: None | object | list
        """
        ...

    def generate(self, table: str | None = None):
        table = table or self.__table
        file = load_datas(file_name="model", file_format="txt", path="modules\\database\\LDB\\templates")
        class_name = table.lower().title()
        table_name = table.lower()
        file = file.replace(":className", class_name)
        file = file.replace(":tableName", table_name)
        create_file(fn=class_name, ff="py", data=file, folder_name="models", rpath="modules\\database\\LDB")
        print(f"Model Created: {class_name}")

    def create(self, data: dict[str, str]) -> None: ...

    def update(self, id: int, data: dict[str, str]) -> None: ...

    def delete(self, id: int) -> None: ...