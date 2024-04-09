from modules.helpers.load_datas import load_datas
from modules.helpers.write_datas import write_datas
from modules.helpers.find_directory import find_directory

class JsonFileWorker:
    def __init__(self):
        __slots__ = ("__virtual_tree", "__config_folder", "__configs", "__version", "__status")
        self.__config_folder: str = find_directory(folder_name="configs")
        self.__configs: dict = dict()
        self.__version: str = "Beta 2.0"
        self.__status = True
        self.__virtual_tree = {}

    def __dynamic_load(self, file_name: str) -> None:
        if file_name in self.__configs: return print("Duplicated")
        try:
            config = load_datas(fn=file_name, ff="json", path=self.__config_folder)
            self.__configs[file_name] = config
            self.__virtual_tree[file_name] = False
        except FileNotFoundError as error: print(error)

    def shutdown(self):
        print("Saving configs...")
        for file_name in self.__configs:
            if self.__virtual_tree[file_name]:
                data = self.__configs[file_name]
                write_datas(datas=data, folder_name=self.__config_folder, fn=file_name, ff="json")
        print("Configs saved")

    def get_config(self, config_file: str, config_key: str | None = None) -> dict | None:
        config_files = [key for key in self.__configs.keys()]
        if config_key:
            if config_file not in config_files:
                self.__dynamic_load(file_name=config_file)
            if config_key not in self.__configs[config_file].items():
                return print(f"{config_key} Not Found In {config_file}")
            return self.__configs[config_file][config_key]
        if config_file not in config_files:
            self.__dynamic_load(file_name=config_file)
        return self.__configs[config_file]

    def set_config(self, config_file: str, config_key: str, config_value: str | int) -> None:
        if config_key not in self.__configs[config_file]: return print("Key Error")
        self.__configs[config_file][config_key] = config_value if config_value not in ["true", "false"] else bool(config_value)
        self.__virtual_tree[config_file] = True

    @property
    def version(self) -> str: return self.__version

    @property
    def status(self) -> bool: return self.__status
