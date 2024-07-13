from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.models.OrderItems import OrderItems

class OrderItemsFactory(Factory):
    def __init__(self):
        super().__init__("order_items")
        self.__count = 6

    def create(self) -> None: ...
