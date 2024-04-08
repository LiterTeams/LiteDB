from modules.database.LDB.system.Model import Model

class User(Model):
    def __init__(self):
        super().__init__("users")

    def create(self, data: dict[str, str]) -> None: super().create(data)

    def update(self, obj_id: int, data: object):
        r"""
        :param obj_id: ...
        :param data:
            nickname: str [required|min:6|max:36],
            email: str [required|unique],
            role: user | moderator | admin [optional],
            password: [required|min:6|max:36|hash],
            created_at: date [optional],
            updated_at: date [optional],
        :return: None
        """
        ...

