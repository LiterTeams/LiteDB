from modules.fileworker.JsonFileWorker import JsonFileWorker

from modules.database.LDB.system.DB import DB
from modules.database.LDB.system.Migration import Migration
from modules.database.LDB.system.Model import Model
from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.system.Seeder import Seeder

from modules.database.LDB.migration.Migrations import Migrations
from modules.database.LDB.models.Models import Models
from modules.database.LDB.factories.Factories import Factories
from modules.database.LDB.seeders.Seeders import Seeders


class LDB:
    def __init__(self):
        self.jfw = JsonFileWorker()
        self.__migrations = Migrations()
        self.models = Models()
        self.__factories = Factories()
        self.__seeders = Seeders()
        self.__configs = None
        self.__status = False

    def migration(self): self.__migrations.run()
    def seeder(self): self.__seeders.run()
    def factory(self): self.__factories.run()

    def fresh(self, use_migration: bool = True, use_seeder: bool = True, use_factory: bool = True):
        if use_migration: self.__migrations.fresh()
        if use_seeder: self.__seeders.run()
        if use_factory: self.__factories.run()

    def start(self, configs: dict):
        self.__configs = configs
        self.__status = True

    @staticmethod
    def merger(): DB().merger()

    def generate(self, table: str) -> None:
        self.generate_migration(table)
        self.generate_model(table)
        self.generate_seeder(table)
        self.generate_factory(table)

    @staticmethod
    def generate_migration(table: str) -> None:
        Migration(table).generate()

    @staticmethod
    def generate_model(table: str) -> None:
        Model(table).generate()

    @staticmethod
    def generate_seeder(table: str) -> None:
        Seeder(table).generate()

    @staticmethod
    def generate_factory(table: str) -> None:
        Factory(table).generate()

    def shutdown(self): self.__status = False

    @property
    def status(self) -> bool: return self.__status
