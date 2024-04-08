from os import walk
from modules.helpers.alias import alias

def find_directory(folder_name: str, base_directory: str | None = None, rpath: str = "assets") -> str:
    if folder_name == rpath: return alias(folder_name)
    try:
        for root, dist, files in walk(alias(rpath + f"\\{base_directory}" if base_directory else rpath)):
            if folder_name in dist:
                return f"{root}\\{folder_name}"
    except TypeError: return ""
