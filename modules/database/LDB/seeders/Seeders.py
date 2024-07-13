from importlib import import_module
from modules.helpers.find_file_new import find_file

class Seeders:
    def __init__(self):
        __slots__ = "__seeders"
        self.__seeders = []
        self.__dynamic_import()

    def __dynamic_import(self):
        files = find_file(ff_whitelist="py", fn_ignore="Seeders", fln_whitelist="seeders", rpath="modules")
        for file in files:
            name = file.get("name")
            path = file.get("path")[17:].replace("\\", ".")
            instance = getattr(import_module(f"{path}.{name}"), name)()
            self.__seeders.append(instance)

    def run(self):
        for seeder in self.__seeders: seeder.run()
