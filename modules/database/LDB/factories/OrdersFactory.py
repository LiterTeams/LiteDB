from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.models.Orders import Orders

class OrdersFactory(Factory):
    def __init__(self):
        super().__init__("orders")
        self.__count = 6

    def create(self) -> None: ...
