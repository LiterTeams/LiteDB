from modules.helpers.find_file import find_file
from modules.helpers.write_datas import write_datas
from modules.helpers.del_file import del_file
from modules.helpers.get_keys import get_keys
from modules.helpers.get_consts import get_consts
from modules.helpers.get_types import get_types
from modules.helpers.get_attributes import get_attributes
from modules.helpers.get_defaults import get_defaults
from modules.helpers.load_datas import load_datas
from modules.helpers.create_file import create_file

from modules.errors.AlreadyExistsError import AlreadyExistsError

class Migration:
    def __init__(self, table: str):
        __slots__ = ("__table", "__columns")
        self.__table: str = table

    def generate(self, table: str | None = None):
        table = table or self.__table
        file = load_datas(file_name="migration", file_format="txt", path="modules\\database\\LDB\\templates")
        class_name = table.lower().title()
        table_name = table.lower()
        file = file.replace(":className", class_name)
        file = file.replace(":tableName", table_name)
        create_file(fn=class_name, ff="py", data=file, folder_name="migration", rpath="modules\\database\\LDB")
        print(f"Migration Created: {class_name}")

    def migration(self, columns: dict[str, str]):
        if find_file(fn=self.__table, **{"multiple_search": True}):
            raise AlreadyExistsError(attribute="migration", value=f"{self.__table} table or types")

        keys = get_keys(columns)
        consts = get_consts(columns)
        defaults = get_defaults(columns)
        types = get_types(columns)
        attributes = get_attributes(columns)
        data = {"keys": keys, "consts": consts, "defaults": defaults, "types": types, "attributes": attributes, "free_id": None}
        write_datas(datas={self.__table: []}, fn=self.__table, ff="json", folder_name="tables")
        write_datas(datas=data, fn=self.__table, ff="json", folder_name="types")

    def drop(self):
        files = find_file(fn=self.__table, **{"multiple_search": True})
        if not files: raise AlreadyExistsError(attribute="migration", value=f"{self.__table} table or types")
        for file in files: del_file(fpath=file)
