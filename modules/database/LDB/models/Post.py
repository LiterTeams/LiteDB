from modules.database.LDB.system.Model import Model

class Post(Model):
    def __init__(self):
        super().__init__("posts")
