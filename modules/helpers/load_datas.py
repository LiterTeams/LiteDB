from json import load
from modules.errors.NotFoundError import NotFoundError

def load_datas(path: str, fn: str | None = None, ff: str | None = None) -> dict | str:
    try:
        if ff == "json":
            if all([fn, ff]):
                with open(f"{path}\\{fn}.{ff}", "r") as file:
                    return load(file)
            else:
                with open(path, "r") as file:
                    return load(file)
        if all([fn, ff]):
            with open(f"{path}\\{fn}.{ff}", "r") as file:
                return file.read()
        else:
            with open(path, "r") as file:
                return file.read()
    except FileNotFoundError:
        raise NotFoundError(value=path, function_name="load datas")
