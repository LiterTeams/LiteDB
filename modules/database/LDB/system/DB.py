import hashlib
from modules.helpers.load_datas import load_datas
from modules.helpers.write_datas import write_datas
from modules.helpers.find_directory import find_directory
from modules.helpers.datetime import datetime
from modules.helpers.auto_search_files import auto_search_files
from modules.helpers.validate import *

class DB:
    def __init__(self, table: str):
        __slots__ = ("__table", "__connect")
        self.__table = table
        self.__data: dict[str,list[dict[str, str]]] | None = None
        self.__types: dict[str, str | list | dict] | None = None
        self.__connect = False

    def __connection(self):
        if self.__data is not None and self.__types is not None or self.__connect: return
        try:
            self.__data = load_datas(fn=self.__table, ff="json", path=find_directory("tables"))
            self.__types = load_datas(fn=self.__table, ff="json", path=find_directory("types"))
            self.__connect = True
        except Exception:
            print("")

    def __disconnection(self):
        if not self.__connect: return
        write_datas(datas=self.__data, fn=self.__table, ff="json", folder_name="tables")
        self.__data = None
        self.__types = None
        self.__connect = False

    def __get_free_id(self) -> int:
        if self.__data.get(self.__table):
            datas_id = set(data.get("id") for data in self.__data.get(self.__table))
            ids = list(set([item for item in range(min(datas_id) - min(datas_id) + 1, max(datas_id) + 1)]).difference(datas_id))
            return ids.pop() if len(ids) > 0 else max(datas_id) + 1
        return 1

    @staticmethod
    def __hash(value) -> str:
        sha256_hash = hashlib.new("sha_256")
        sha256_hash.update(value.encode())
        return sha256_hash.hexdigest()

    def __unique_check(self, value: str | int) -> bool:
        for data_item in self.__data.get(self.__table):
            for key, data_value in data_item.items():
                if data_value == value: return False
        return True

    @staticmethod
    def merger(): ...

    def query(self, **params) -> None | object | list:
        r"""
        :param params:
            search: str [optional],
            order_by: asc | desc [optional],
            paginate: int [optional],
        :return: None | object | list
        """
        self.__connection()
        self.__disconnection()


    def create(self, data: dict[str, str]):
        self.__connection()
        id = self.__get_free_id()
        date = datetime(self.__types.get("attributes").get("created_at"))
        for key, value in data.items():
            if not type_check(value, self.__types.get("types").get(key)): raise Exception(f"table:{self.__table} | type: {key}")
            if "unique" in self.__types.get("attributes").get(key) and not self.__unique_check(value): raise Exception(f"table:{self.__table} | type: {key}")
            if "enum" in self.__types.get("attributes").get(key) and not enum_check(value, self.__types.get("attributes").get(key)): raise Exception("Enum Error")
            for default in self.__types.get("defaults"):
                if default == "role" and default not in data:
                    default = self.__types.get("attributes").get("role").split("|")
                    default = ",".join([i.split("default")[1].split("[")[1].split("]")[0] for i in default if i.startswith("default")])
                    data = data | {"role": default}
        data = {"id": id} | data
        data = data | {"created_at": date, "updated_at": date}
        self.__data.get(self.__table).append(data)
        self.__disconnection()

    def update(self, object_id: int, data: dict[str, str]):
        self.__connection()
        self.__disconnection()

    def delete(self, object_id: int):
        self.__connection()
        self.__disconnection()
