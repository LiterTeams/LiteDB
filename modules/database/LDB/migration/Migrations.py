from modules.database.LDB.migration.Users import Users
from modules.database.LDB.migration.Posts import Posts
from modules.database.LDB.migration.News import News

class Migrations:
    def __init__(self):
        self.__migrations = [Users(), Posts(), News()]

    def run(self):
        for migration in self.__migrations:
            migration.up()

    def fresh(self):
        for migration in self.__migrations:
            migration.fresh()