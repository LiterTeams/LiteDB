from modules.database.LDB.models.User import User
from modules.database.LDB.models.Post import Post
from modules.database.LDB.models.News import News

class Models:
    def __init__(self):
        self._users = User()
        self._posts = Post()
        self._news = News()
