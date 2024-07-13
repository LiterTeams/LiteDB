from modules.database.Database import Database

if __name__ == "__main__":
    database = Database()
    # database.lite_db.migration()
    # database.lite_db.seeder()
    # database.lite_db.factory()
    response = database.lite_db.models.products.query()
    # data = {
    #     "catalog_id": 2,
    #     "category_id": 2,
    #     "title": "Test Create",
    #     "image": "",
    #     "price": 24,
    # }
    # database.lite_db.models.products.create(data)
    # data = {
    #     "title": "New New Test Title",
    # }
    # database.lite_db.models.products.update(87, data)
    #database.lite_db.models.products.delete(87)
    # for i in response.get("data"):
    #     print(i)
    database.shutdown()
