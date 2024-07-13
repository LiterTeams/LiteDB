from importlib import import_module
import re
from modules.helpers.find_file_new import find_file

class Models:
    def __init__(self): self.__dynamic_import()

    def __dynamic_import(self):
        files = find_file(ff_whitelist="py", fn_ignore="Models", fln_whitelist="models", rpath="modules")
        for file in files:
            res = re.findall("[A-Z][^A-Z]*", file.get("name"))
            attr = "".join(res).lower() if len(res) == 1 else "_".join(res).lower()
            name = attr.title()
            path = file.get("path")[17:].replace("\\", ".")
            instance = getattr(import_module(f"{path}.{name if '_' not in name else name.replace('_', '')}"), name if "_" not in name else name.replace("_", ""))()
            self.__setattr__(attr, instance)
