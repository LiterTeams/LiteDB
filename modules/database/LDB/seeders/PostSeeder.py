from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.Post import Post


class PostSeeder(Seeder):
    def __init__(self):
        super().__init__("posts")
        self.__data = [
            {
                "user_id": 1,
                "title": "Test Title 1",
                "image": "https://sun1-17.userapi.com/impg/5rfC3ntC9cvHMOordSAKdaI1nSXmLioV1O0nTw/rsqzc8X9Sn4.jpg?size=624x920&quality=95&sign=3781f4127c7007e5b1b44d857abaffc6&type=album",
            },
            {
                "user_id": 2,
                "title": "Test Title 2",
                "image": "https://sun1-55.userapi.com/impg/rx4MmlaTit51HWN_9qE5LkawN6GMimH1aVQCBg/oKOa_2m5Kig.jpg?size=653x920&quality=95&sign=bad5a8cdf437f4b82445c147a6114709&type=album",
            },
            {
                "user_id": 3,
                "title": "Test Title 3",
                "image": "https://sun1-84.userapi.com/impg/yFHHXd4qDOYEiJF6iNcT0nldcVgQmoe_W-P3QQ/SnRDnnMIM1Y.jpg?size=635x880&quality=95&sign=b1cf06b43154d1f8fa487fec9f42473f&type=album",
            }
        ]

    def run(self):
        for data_item in self.__data: Post().create(data_item)
