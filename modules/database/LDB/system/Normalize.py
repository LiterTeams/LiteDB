import hashlib
from modules.helpers.datetime import datetime


class Normalize:
    def __init__(self, table: str):
        __slots__ = "__table"
        self.__table = table

    @staticmethod
    def __hash(value) -> str:
        sha256_hash = hashlib.new("sha256")
        sha256_hash.update(value.encode())
        return sha256_hash.hexdigest()

    def _normalize(self, types: dict[str, str | list | dict], data: dict[str, str]) -> dict:
        for key, value in data.items():
            if "hash" in types.get("attributes").get(key):
                data[key] = self.__hash(value)
            for default in types.get("defaults"):
                if default == "role" and default not in data:
                    default = types.get("attributes").get("role").split("|")
                    default = ",".join([i.split("default")[1].split("[")[1].split("]")[0] for i in default if i.startswith("default")])
                    data = data | {"role": default}
        date = datetime(types.get("attributes").get("created_at"))
        data = data | {"created_at": date, "updated_at": date}
        return data
