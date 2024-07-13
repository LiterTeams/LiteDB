from modules.database.LDB.system.Decorators import GET, POST, PATCH, DELETE, SERVICE
from modules.database.LDB.services.TestService import TestService

@SERVICE("test")
class TestController:
    def __init__(self):
        self.__test_service = TestService()

    @GET()
    def get_all(self): ...

    @GET(":id")
    def get_one(self, id: str): ...

    @POST()
    def create(self, data: any): ...

    @PATCH(":id")
    def update(self, id: str, data: any): ...

    @DELETE(":id")
    def delete(self, id: str): ...
