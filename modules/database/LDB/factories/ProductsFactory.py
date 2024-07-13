from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.system.Faker import Faker
from modules.database.LDB.models.Products import Products
from modules.database.LDB.models.Categories import Categories
from modules.database.LDB.models.Catalogs import Catalogs

class ProductsFactory(Factory):
    def __init__(self):
        super().__init__("products")
        self.__faker = Faker()
        self.__count = 86

    def create(self) -> None:
        for i in range(self.__count):
            category = Categories().query(use_random=True, limit=1).get("data")[0]
            catalog = Catalogs().query(use_random=True, limit=1).get("data")[0]
            image = self.__faker.image()
            title = self.__faker.text()
            category_id = category.get("id")
            catalog_id = catalog.get("id")
            price = 3630
            discount = "0%"
            data = {"category_id": category_id, "catalog_id": catalog_id, "image": image, "title": title, "price": price, "discount": discount}
            Products().create(data)
