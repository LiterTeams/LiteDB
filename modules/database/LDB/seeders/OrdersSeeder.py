from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.Orders import Orders


class OrdersSeeder(Seeder):
    def __init__(self):
        super().__init__("orders")
        __slots__ = "__data"
        self.__data: list[dict] = []

    def run(self):
        if len(self.__data) == 0: return
        for data_item in self.__data: Orders().create(data_item)
