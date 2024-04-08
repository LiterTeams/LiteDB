from modules.helpers.find_directory import find_directory

def create_file(fn: str, ff: str, base_directory: str | None = None, folder_name: str | None = None, data: str | None = None, rpath: str | None = None) -> None:
    try:
        if rpath:
            with open(f"{find_directory(folder_name=folder_name, base_directory=base_directory, rpath=rpath)}\\{fn}.{ff}", "w") as file:
                file.write(data if data else "{}")
        with open(f"{find_directory(folder_name=folder_name)}\\{fn}.{ff}", "w") as file:
            file.write(data if data else "{}")
    except FileNotFoundError as error: ...

