from os import walk
from modules.helpers.alias import alias

def _find_project(disk: str = "/", project: str = "") -> str | None:
    for root, dirs, files in walk(disk):
        if project in dirs: return f"{alias(root)}\\{project}"
    return None
