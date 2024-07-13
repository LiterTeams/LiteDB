from importlib import import_module
from modules.helpers.find_file_new import find_file


class Migrations:
    def __init__(self):
        __slots__ = "__migrations"
        self.__migrations = []
        self.__dynamic_import()

    def __dynamic_import(self):
        files = find_file(ff_whitelist="py", fn_ignore="Migrations", fln_whitelist="migration", rpath="modules")
        for file in files:
            name = file.get("name")
            path = file.get("path")[17:].replace("\\", ".")
            instance = getattr(import_module(f"{path}.{name}"), name)()
            self.__migrations.append(instance)

    def run(self):
        for migration in self.__migrations:
            migration.up()

    def fresh(self):
        for migration in self.__migrations:
            migration.fresh()
