from functools import reduce

from modules.database.LDB.system.Validate import Validate
from modules.database.LDB.system.Normalize import Normalize

from modules.helpers.load_datas import load_datas
from modules.helpers.write_datas import write_datas
from modules.helpers.find_directory import find_directory
from modules.helpers.find_file import find_file

from modules.helpers.filter import *

from modules.errors.NotFoundError import NotFoundError


class DB(Validate, Normalize):
    def __init__(self, table: str | None = None):
        __slots__ = ("__table", "__data", "__types", "__limit_default", "__connect", "__changed")
        super().__init__(table)
        self.__table = table
        self.__data: dict[str, list[dict[str, str | int]]] | None = None
        self.__types: dict[str, str | list | dict] | None = None
        self.__limit_default = 24
        self.__connect = False
        self.__changed = False

    def __connection(self):
        if self.__data is not None and self.__types is not None or self.__connect: return
        try:
            self.__data = load_datas(fn=self.__table, ff="json", path=find_directory("tables"))
            self.__types = load_datas(fn=self.__table, ff="json", path=find_directory("types"))
            self.__connect = True
        except FileNotFoundError: ...

    def __disconnection(self):
        if not self.__connect: return
        if self.__changed: write_datas(datas=self.__data, fn=self.__table, ff="json", folder_name="tables")
        self.__data = None
        self.__types = None
        self.__connect = False
        self.__changed = False

    def __get_free_id(self) -> int:
        try:
            if self.__data.get(self.__table):
                datas_id = set(data.get("id") for data in self.__data.get(self.__table))
                ids = list(
                    set([item for item in range(min(datas_id) - min(datas_id) + 1, max(datas_id) + 1)]).difference(
                        datas_id))
                return ids.pop() if len(ids) > 0 else max(datas_id) + 1
            return 1
        except AttributeError:
            raise NotFoundError(f"table: {self.__table} | Use Migration")

    @staticmethod
    def merger() -> None:
        data = dict()
        tables = find_file(ff_whitelist="json", fln_blacklist=["private", "types"], fln_whitelist=["LDB", "tables"])
        for table in tables:
            data |= load_datas(path=table, ff="json")
        write_datas(datas=data, ff="json", fn="data", folder_name="tables")

    # @staticmethod
    # def __get_by_id(data: list[dict], id: int) -> dict:
    #     result = list(filter(lambda data_item: data_item.get("id") == id, data))
    #     return result[0] if len(result) == 1 else dict()
    #
    # @staticmethod
    # def __get_by_search(data: list[dict], search: str) -> list[dict]:
    #     ...
    #
    # @staticmethod
    # def __random(data: list[dict], random: int) -> dict[str, list[Any] | dict[str, int]]:
    #     random = random if random > len(data) | random < len(data) else len(data)
    #     response = {"data": list(), "meta": {"pages": 1, "items": 0, "total_items": 0}}
    #     for i in range(random):
    #         if len(data) == 1:
    #             response.get("data").append(data.pop())
    #             break
    #         else:
    #             response.get("data").append(data.pop(randint(0, len(data) - 1)))
    #     items = len(response.get("data"))
    #     response.get("meta").update(items=items, total_items=items)
    #     return response
    #
    #
    # @staticmethod
    # def __paginate(data: list[dict], paginate: int) -> dict[str, list[Any] | dict[str, int]]:
    #     response = {"data": list(), "meta": {"pages": 1, "items": 0, "total_items": 0}}
    #     if paginate <= 0: return response
    #
    #     for index, data_item in enumerate(data, start=1):
    #         if index > paginate: break
    #         response.get("data").append(data_item)
    #
    #     items = len(response.get("data"))
    #     total_items = len(data)
    #     pages = ceil(total_items / items)
    #     response.get("meta").update(pages=pages, items=items, total_items=total_items)
    #
    #     return response

    def query(self, **params) -> list[dict] | dict:
        r"""
        Порядок передачи параметров не важем.
        При использовании use_random, пагинация не работает.
        *если limit == 0, то use_random проигнорируется.
        :param params:
            id: int [optional],
            search: str [optional],
            use_random: bool [optional] | default - False
            limit: int [optional] | default - self.__limit_default,
            order_by: asc | desc [optional] | default - desc,
            paginate: int [optional],
        :return:  dict | list[dict]
        """
        response = {"data": [], "meta": {"pages": 1, "items": 0, "total_items": 0}}
        self.__connection()
        if not self.__connect: return response

        id: int | None = params.get("id", None)
        use_random: bool = params.get("use_random", False)
        limit: int | None = params.get("limit", self.__limit_default)
        order_by: dict = params.get("order_by", {"id": "desc"})
        paginate: int | None = params.get("paginate", None)
        data = self.__data.get(self.__table)

        if id: return get_by_id(data, id)
        if use_random and limit != 0: return random(data, limit)
        if order_by: data = order_by_filter(data, order_by)
        if paginate: data = paginating(data.get("data"), paginate)
        self.__disconnection()
        return data

    def create(self, data: dict[str, str]):
        self.__connection()
        if not self.__connect: return
        self._validate(self.__data, self.__types, data)
        data = self._normalize(self.__types, data)
        data = {"id": self.__get_free_id()} | data
        self.__data.get(self.__table).append(data)
        self.__changed = True
        self.__disconnection()

    def update(self, id: int, data: dict[str, str]) -> None:
        self.__connection()
        if not self.__connect: return
        self._validate(self.__data, self.__types, data)
        data = self._normalize(self.__types, data)
        data = {key: value for key, value in data.items() if key not in self.__types.get("consts")}
        data_item = self.query(id=id)
        for key, value in data.items(): data_item.update({key: value})
        self.__changed = True
        self.__disconnection()

    def delete(self, id: int) -> None:
        self.__connection()
        if not self.__connect: return
        for index in range(len(self.__data.get(self.__table))):
            if self.__data.get(self.__table)[index].get("id") == id:
                del self.__data.get(self.__table)[index]
                break
        self.__changed = True
        self.__disconnection()
