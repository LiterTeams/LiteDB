from importlib import import_module
from modules.helpers.find_file_new import find_file

class Factories:
    def __init__(self):
        __slots__ = "__factories"
        self.__factories = []
        self.__dynamic_import()

    def __dynamic_import(self):
        files = find_file(ff_whitelist="py", fn_ignore="Factories", fln_whitelist="factories", rpath="modules")
        for file in files:
            name = file.get("name")
            path = file.get("path")[17:].replace("\\", ".")
            instance = getattr(import_module(f"{path}.{name}"), name)()
            self.__factories.append(instance)

    def run(self):
        for factory in self.__factories: factory.create()
