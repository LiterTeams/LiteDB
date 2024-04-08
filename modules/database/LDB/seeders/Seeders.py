from modules.database.LDB.seeders.UserSeeder import UserSeeder
from modules.database.LDB.seeders.PostSeeder import PostSeeder
from modules.database.LDB.seeders.NewsSeeder import NewsSeeder

class Seeders:
    def __init__(self):
        self.__seeders = [UserSeeder(), PostSeeder(), NewsSeeder()]

    def run(self):
        for seeder in self.__seeders:
            seeder.run()

    def fresh(self): ...
