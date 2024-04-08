from modules.fileworker.JsonFileWorker import JsonFileWorker

from modules.database.LDB.system.Migration import Migration
from modules.database.LDB.system.Model import Model
from modules.database.LDB.system.Factory import Factory
from modules.database.LDB.system.Seeder import Seeder

from modules.database.LDB.migration.Migrations import Migrations
from modules.database.LDB.factories.Factories import Factories
from modules.database.LDB.seeders.Seeders import Seeders

from modules.helpers.auto_search_files import auto_search_files

class LDB:
    def __init__(self):
        self.jfw = JsonFileWorker()
        self.__migrations = Migrations()
        self.__factories = Factories()
        self.__seeders = Seeders()
        self.__configs = None
        self.__tables = None
        self.__types = None
        self.__status = False

    def migration(self): self.__migrations.run()
    def seeder(self): self.__seeders.run()
    def factory(self): self.__factories.run()

    def fresh(self, use_migration: bool = True, use_seeder: bool = True, use_factory: bool = True):
        if use_migration: self.__migrations.fresh()
        if use_seeder: self.__seeders.fresh()
        if use_factory: self.__factories.fresh()

    def start(self, configs: dict):
        self.__configs = configs
        # tables = auto_search_files(folder_name="tables", fln_blacklist=["private"], fln_whitelist=["LDB"])
        # types = auto_search_files(folder_name="types", fln_blacklist=["private"], fln_whitelist=["LDB"])
        self.__status = True

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

    def shutdown(self):
        self.__status = False

    @property
    def status(self) -> bool: return self.__status
