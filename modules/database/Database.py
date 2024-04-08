from modules.fileworker.JsonFileWorker import JsonFileWorker
from modules.database.LDB.LDB import LDB
from modules.database.SQLDB.SQLDB import SQLDB
from modules.database.MSQLDB.MSQLDB import MSQLDB
from modules.database.PDB.PDB import PDB
from modules.database.Supabase.SupabaseDB import SupabaseDB

class Database:
    def __init__(self):
        self.jfw = JsonFileWorker()
        self.root_config = "database"
        self.lite_db = LDB()
        self.sqllite_db = SQLDB()
        self.mysql_db = MSQLDB()
        self.postgres_db = PDB()
        self.supabase_bd = SupabaseDB()
        self.database = None
        self.database_config: dict | None = None

    def __config_init(self):
        self.database_config = self.jfw.get_config(self.root_config)
        if self.database_config.get("current_db"): return
        print(f"supported database: {self.database_config.get('supports_db')}")
        self.jfw.set_config(self.root_config, "current_db", input("DB: "))

    def __services_init(self):
        db_name: str = self.database_config.get("current_db")
        match db_name:
            case "Lite": self.lite_db.start(self.jfw.get_config(db_name))
            case "SQL": self.sqllite_db.start(self.jfw.get_config(db_name))
            case "MSQL": self.mysql_db.start(self.jfw.get_config(db_name))
            case "Postgres": self.postgres_db.start(self.jfw.get_config(db_name))
            case "Supabase": self.supabase_bd.start(self.jfw.get_config(db_name))
            case _: print(f"Unsupported DataBase: {self.database_config.get(db_name)}")

    def start(self):
        self.__config_init()
        self.__services_init()

    def shutdown(self):
        self.jfw.shutdown()
        try:
            match self.database_config.get("current_db"):
                case "Lite": self.lite_db.shutdown()
                case "SQL": self.sqllite_db.shutdown()
                case "MSQL": self.mysql_db.shutdown()
                case "Postgres": self.postgres_db.shutdown()
                case "Supabase": self.supabase_bd.shutdown()
                case _: print("Error")
        except AttributeError: print("Error")
