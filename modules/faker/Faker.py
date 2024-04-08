

class Faker:
    def __init__(self):
        self.__images = [
            "https://sun9-73.userapi.com/impg/5rfC3ntC9cvHMOordSAKdaI1nSXmLioV1O0nTw/rsqzc8X9Sn4.jpg?size=624x920&quality=95&sign=3781f4127c7007e5b1b44d857abaffc6&type=album",
            "https://sun9-61.userapi.com/impg/62dPhCSkf-5dTm0IfrthpgbcD13RWstYLTLmvA/HRR6Gyit2z8.jpg?size=978x1400&quality=96&sign=44743644323e9ffd94a0ce06f2aa8fb9&type=album",
            "https://sun1-90.userapi.com/impg/5aHhNsMTGHUxaoRHr3W9tganGsRgyDoJ6PahjA/Vra7KbfdKvE.jpg?size=1627x2160&quality=95&sign=91df90910938d5f23c315f15bce50750&type=album",
            "https://sun9-55.userapi.com/impg/ZF7FAEeA0R7NDtjXQxC4tkBnAG4fai0IB9QIZQ/4oz8oEft0nM.jpg?size=1439x2003&quality=95&sign=56ace62810dd911c686ab4f2cd69f425&type=album",
            "https://sun9-13.userapi.com/impg/7QOsMcGu3c-84ltUCWCcK0vN8Tlo7WDlW8zQqg/aj35kO1gPJ8.jpg?size=698x1000&quality=96&sign=a41693a29c0d892b8ccb37add63f8bda&type=album",
            "https://sun1-25.userapi.com/impg/IhIrP5M2p10cx-kCbNcovHS_Xxl_6epw1-vadA/R4ShF3iRSxs.jpg?size=1574x2160&quality=95&sign=fc1d72fdb0ce523d768e679dfb170c6a&type=album",
            "https://sun9-1.userapi.com/impg/7UIx2vdh5W59N-WKsPmU2vkAXVQsOYkcYoen0Q/jDQ_Sn7JVB0.jpg?size=2560x1406&quality=95&sign=d7bf814108c3b160ff6fd495e5157d8d&type=album",
            "https://sun9-43.userapi.com/impg/tOuvYy3eh_15KRyitePl1hKQZUWZyCjGWuyVkg/_5wA5k-flT4.jpg?size=1545x1599&quality=95&sign=2db3a398e912caf0ddbbfe9556afc564&type=album",
            "https://sun9-27.userapi.com/impg/5Hksd4yBtKrkmLIKcLRaKSkPk4ygDtWAy_5atw/SpPY2X2OlcU.jpg?size=1600x1196&quality=95&sign=53c2547627032ccdb78e31b4829f6712&type=album",
            "https://sun1-13.userapi.com/impg/kW2VKo7EjRwSxGULZjPflH21Earyv5ZOIo0ltw/1AkvUuyzw0o.jpg?size=2560x1807&quality=96&sign=4b8f56e340c5bb8b07bcea28434bf934&type=album",
            "https://sun9-24.userapi.com/impg/UzG2BcY2xW6H5ENzEFk6vSb6eKOE6Wh1M3tsoQ/nwIhr-0FIak.jpg?size=2088x1514&quality=96&sign=345be2a6741a63289820a25a248db30a&type=album",
            "https://sun1-98.userapi.com/impg/VPLax3suvzA9IVNsPoLmeAB7ac0wtKPzkEVnUQ/1_MkGxeYzKI.jpg?size=1920x1080&quality=95&sign=9ca55f1c0bb0648c13f92d9ccb6aa95a&type=album",
            "https://sun1-54.userapi.com/impg/00qedWVXI-ZHV_tPnZEizvDdKZN7J5ZlvHK77A/ZazOa4K2gKg.jpg?size=928x1232&quality=96&sign=dbb26dea2009dbc9c2d3cbb15dc075b3&type=album",
            "https://sun1-87.userapi.com/impg/0PT6Ubf5BgEwHDSSdUoXYtCsUdin-IZUPXXeBg/RyefvB-JsJo.jpg?size=2310x1300&quality=95&sign=8c5736f3269826fe32a1fc2e73854cbd&type=album",
        ]

    def image(self) -> str: ...

    def password(self) -> str: ...

    def timestamp(self) -> str: ...
