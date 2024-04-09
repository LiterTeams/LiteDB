from modules.database.LDB.seeders.UserSeeder import UserSeeder
from modules.database.LDB.seeders.PostSeeder import PostSeeder

class Seeders:
    def __init__(self):
        self.__seeders = [UserSeeder(), PostSeeder()]

    def run(self):
        for seeder in self.__seeders:
            seeder.run()

    def fresh(self): ...
