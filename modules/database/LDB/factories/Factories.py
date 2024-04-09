from modules.database.LDB.factories.UserFactory import UserFactory
from modules.database.LDB.factories.PostFactory import PostFactory

class Factories:
    def __init__(self):
        self.__factories = [UserFactory(), PostFactory()]

    def run(self):
        for factory in self.__factories:
            factory.create(6)

    def fresh(self): ...
