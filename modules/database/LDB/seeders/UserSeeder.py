from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.User import User


class UserSeeder(Seeder):
    def __init__(self):
        super().__init__("users")
        __slots__ = "__data"
        self.__data: list[dict] = [
            {
                "nickname": "Salfiya NSFW",
                "email": "salfiy.nsfw@gmail.com",
                "password": "password",
                "role": "admin",
            },
            {
                "nickname": "Thunder Light",
                "email": "thunder.light@gmail.com",
                "password": "password",
                "role": "moderator",
            },
            {
                "nickname": "Selenium",
                "email": "selenium@gmail.com",
                "password": "password",
            }
        ]

    def run(self):
        if len(self.__data) == 0: return
        for data_item in self.__data: User().create(data_item)
