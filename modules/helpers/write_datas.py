from json import dump
from modules.helpers.find_directory import find_directory
from modules.errors.NotFoundError import NotFoundError

def write_datas(datas: dict, folder_name: str, fn: str | None = None, ff: str | None = None) -> None:
    try:
        if all([fn, ff]):
            with open(f"{find_directory(folder_name)}\\{fn}.{ff}", "w") as file:
                dump(datas, file, indent=None, separators=(",", ":"), ensure_ascii=False)
        else:
            with open(find_directory(folder_name), "w") as file:
                dump(datas, file, indent=None, separators=(",", ":"), ensure_ascii=False)
    except FileNotFoundError:
        raise NotFoundError(message=f"folder: {folder_name} | write datas")
