from modules.database.LDB.system.Model import Model

class User(Model):
    def __init__(self):
        super().__init__("users")
