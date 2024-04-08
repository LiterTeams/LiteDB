from json import load
from modules.errors.NotFoundError import NotFoundError

def load_datas(path: str, file_name: str | None = None, file_format: str | None = None) -> dict | str:
    try:
        if file_format == "json":
            if all([file_name, file_format]):
                with open(f"{path}\\{file_name}.{file_format}", "r") as file:
                    return load(file)
            else:
                with open(path, "r") as file:
                    return load(file)
        if all([file_name, file_format]):
            with open(f"{path}\\{file_name}.{file_format}", "r") as file:
                return file.read()
        else:
            with open(path, "r") as file:
                return file.read()
    except FileNotFoundError:
        raise NotFoundError(value=path, function_name="load datas")
