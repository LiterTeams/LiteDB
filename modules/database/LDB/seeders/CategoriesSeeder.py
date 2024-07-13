from modules.database.LDB.system.Seeder import Seeder
from modules.database.LDB.models.Categories import Categories


class CategoriesSeeder(Seeder):
    def __init__(self):
        super().__init__("categories")
        __slots__ = "__data"
        self.__data: list[dict] = [
            {"catalog_id": 1, "category": "monitors", "image": "https://sun9-70.userapi.com/impg/FIjjpWfF5-zL894snprcCdEInav4tKY8AzomlA/TDyIy5M2U1A.jpg?size=960x1040&quality=96&sign=5bc6eebf4b2088cb0c60765ad5a143a1&type=album"},
            {"catalog_id": 1, "category": "periphery", "image": "https://sun1-18.userapi.com/impg/e712_xEVFOeudSHsKSs0TuVxOLpxglbRgOdmew/4qhXA1XfmGY.jpg?size=1496x2160&quality=95&sign=d3987e5c9cbc1420a5d58318775c0b52&type=album"},
            {"catalog_id": 1, "category": "system units", "image": "https://sun9-12.userapi.com/impg/NdC7b0lrMZA7rIvlYe4UpS4OC_54LnnWcvPccQ/7aukPyEgv3o.jpg?size=2560x1576&quality=95&sign=2fdf5cff4af79228c4939439fd1802d3&type=album"},
            {"catalog_id": 1, "category": "laptops", "image": "https://sun9-36.userapi.com/impg/ah3SmjLy9QrA9WiSetMflvcNjWiJzptvEviSiQ/p7WxC8XS_74.jpg?size=850x618&quality=96&sign=2bb94363a57aaa9c1d396a29fa3f8732&type=album"},
            {"catalog_id": 1, "category": "network hardware", "image": "https://sun9-79.userapi.com/impg/ReH3NHxf4AlgLOjLy5RPijy1cjRXkEEbQwhi1g/-xpvWKfPgWM.jpg?size=1200x840&quality=95&sign=87b4f5d056ec25d7bd2d5919b175b491&type=album"},
            {"catalog_id": 1, "category": "accessories", "image": "https://sun9-11.userapi.com/impg/CRXJRy8I390MPTwvDyjjiLTpbOs9GwqObMMdMQ/uU-6VP8EKAE.jpg?size=2560x1700&quality=95&sign=808c6c25e541c05d3a99d1deab0a69f8&type=album"},

            {"catalog_id": 2, "category": "antivirus programs", "image": "https://sun9-55.userapi.com/impg/ZF7FAEeA0R7NDtjXQxC4tkBnAG4fai0IB9QIZQ/4oz8oEft0nM.jpg?size=1439x2003&quality=95&sign=56ace62810dd911c686ab4f2cd69f425&type=album"},
            {"catalog_id": 2, "category": "utilities", "image": "https://sun9-3.userapi.com/impg/s88IlVQ0l9BtIA7aLSDo5-Q4P8xgPox-Lso28w/H4j6XtOJKlQ.jpg?size=825x1168&quality=96&sign=4bcac3daf9cfaf78dd64b9037f196959&type=album"},

            {"catalog_id": 3, "category": "usb", "image": "https://sun9-13.userapi.com/impg/bGb6wWgxTVsmCb5eW5rcCgqQn0AM21VS5t7DxA/X9TxjE5NAUk.jpg?size=1280x761&quality=96&sign=72711133f08082d2cb4c40179d678786&type=album"},
            {"catalog_id": 3, "category": "audio/video cables", "image": "https://sun9-14.userapi.com/impg/qy8mtS1Nh-g6uFoGdj_SlKcDmWy_czBxNY3pkg/JcA3D6w-2cw.jpg?size=1280x776&quality=96&sign=bd3313b8e9107d3648d38d05c0dd1082&type=album"},
            {"catalog_id": 3, "category": "monitor cables", "image": "https://sun9-65.userapi.com/impg/Cpl2dAMPWDSOJnVgBCGnZXGntdJkbWLJny2dEQ/k3XkyZlG4YU.jpg?size=1080x1578&quality=95&sign=073c597ce8e48305cd25b165ae404c5e&type=album"},
            {"catalog_id": 3, "category": "adapters", "image": "https://sun9-50.userapi.com/impg/82Rnio3H4ANZdJJz181cLQmgosRCN76Ozg60Qg/8dYNYT_CvIY.jpg?size=1080x1578&quality=95&sign=9171fc1051cfed2be990c0590f899587&type=album"},
            {"catalog_id": 3, "category": "power cords", "image": "https://sun9-19.userapi.com/impg/VKoM53zpc0xjcFd8HJVmpV9ceD6eUcg-8uqAPA/77zsUa9WruI.jpg?size=1080x1578&quality=95&sign=ca65f9a4d75d380c8e942231e33437cd&type=album"},
            {"catalog_id": 3, "category": "extension cords", "image": "https://sun9-57.userapi.com/impg/9pRNLGWmUwaooibC1wEwYqVITLZ1RlD8f4Yy3w/yxoJV4nGNis.jpg?size=2560x1997&quality=96&sign=4d8160e246c61df5939dbdb017bb1db1&type=album"},

            {"catalog_id": 4, "category": "patriot", "image": "https://sun9-39.userapi.com/impg/edzadFAzUoYS7sgHIkF8zQpA8kZ3bE1Ygjsnbg/6E0F3iE1flk.jpg?size=1700x1202&quality=95&sign=bf1cd11b191ec939211a7ef9eecd6808&type=album"},

            {"catalog_id": 5, "category": "computer tables", "image": "https://sun9-21.userapi.com/impg/w5njZiKIM-zKLSbL5NZ8iJNAlgVhR4KlM2Oytg/e-DB6zIBrY8.jpg?size=1706x1228&quality=95&sign=228f8bcdffc16fdf10979c2dc78ae968&type=album"},
            {"catalog_id": 5, "category": "armchairs", "image": "https://sun9-53.userapi.com/impg/novKF-iIB18QM-QnymNwzct5f9E57lRt8pDKUA/n4ofWfx4s3U.jpg?size=2400x1580&quality=95&sign=9c91056d81b9fc7701f6465b93e47a39&type=album"},
            {"catalog_id": 5, "category": "furniture accessories", "image": "https://sun9-77.userapi.com/impg/R-qp9sZi2HmKFOnoo7MzHVZowhdj4zDyNnFZww/KJNVagCvdNQ.jpg?size=1700x950&quality=95&sign=4ec6b13391da11112a3590c22e7aea96&type=album"},
            {"catalog_id": 5, "category": "shelves", "image": "https://sun9-37.userapi.com/impg/ZEBKNOPWCG6QYfLaWLEzgS85N0_btZo7a2R5qw/YeS6l03pQoM.jpg?size=2044x2160&quality=95&sign=f515de332b8e373bb75faada29aeb1c1&type=album"},

            {"catalog_id": 6, "category": "patriot", "image": "https://sun9-20.userapi.com/impg/u3sSMmBoKEIrWGD4nQ2bRTNBKuNzQH30neak6A/RUGJelWS588.jpg?size=2560x2560&quality=95&sign=d1dd993ff4bb35ee325d9d57cda8b486&type=album"},

            {"catalog_id": 7, "category": "toners", "image": "https://sun9-32.userapi.com/impg/h-_h9OkHR09vHDKWROlMHuBlGJjoisz9eAxnHg/aL4N8fKD-QI.jpg?size=2560x1604&quality=95&sign=0a3b8eb5e99a92ae2ee7eb01b6375095&type=album"},
            {"catalog_id": 7, "category": "cartridges", "image": "https://sun9-14.userapi.com/impg/6i30DCUZIugjy316uCTPL7duvXXrwGu8ae0ntQ/AbTiz5Vbz4s.jpg?size=2560x1889&quality=95&sign=8ba56a1abcc98881082aeaf676cce861&type=album"},
            {"catalog_id": 7, "category": "batteries", "image": "https://sun9-2.userapi.com/impg/xdW70bJ5pSWZgJ46hPXfPUHv8PQ-x8mBqJUo6w/kZ0Yh8RyzLQ.jpg?size=1700x1062&quality=95&sign=8eac6d8a5dbae8fc6f5fdf77bffe81aa&type=album"},
            {"catalog_id": 7, "category": "paper", "image": "https://sun9-12.userapi.com/impg/qdVo9D9IK23J07HGSX57mfP-nk_Dr0s0PaIiZQ/Co4G0tIg6i8.jpg?size=1700x1276&quality=95&sign=556acf6c019096338c2aa9f815dc56c8&type=album"},
            {"catalog_id": 7, "category": "CD/DVD", "image": "https://sun9-47.userapi.com/impg/Vx_OIDWFRyunPNuiXI3Qaws0eE6E2iSkseFJSg/CdsCWSdj5oo.jpg?size=1700x1402&quality=95&sign=8ba0f7418c8c82098f1bdf1004ce39aa&type=album"},
        ]

    def run(self):
        if len(self.__data) == 0: return
        for data_item in self.__data: Categories().create(data_item)
