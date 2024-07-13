from modules.helpers.validate import type_check, enum_check

class Validate:
    def __init__(self, table: str):
        __slots__ = "__table"
        self.__table = table

    def __unique_check(self, all_data: dict[str, list[dict[str, str]]], value: str | int) -> bool:
        for data_item in all_data.get(self.__table):
            for key, data_value in data_item.items():
                if data_value == value: return False
        return True

    def _validate(self, all_datas: dict[str, list[dict[str, str]]], types: dict[str, str | list | dict], data: dict[str, str]) -> None:
        for key, value in data.items():
            if key not in types.get("types"): raise Exception(f"table:{self.__table} | type: {key} does not exist in attributes")
            if not type_check(value, types.get("types").get(key)): raise Exception(f"table:{self.__table} | type: {key} impossible to change")
            if "unique" in types.get("attributes").get(key) and not self.__unique_check(all_datas, value): raise Exception(f"table:{self.__table} | type: {key}")
            if "enum" in types.get("attributes").get(key) and not enum_check(value, types.get("attributes").get(key)): raise Exception(f"table:{self.__table} | type: {key} does not match the passed result")
