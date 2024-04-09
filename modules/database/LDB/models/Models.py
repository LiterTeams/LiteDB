from modules.database.LDB.models.User import User
from modules.database.LDB.models.Post import Post

class Models:
    def __init__(self):
        self._users = User()
        self._posts = Post()
