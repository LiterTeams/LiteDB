from modules.database.Database import Database


if __name__ == "__main__":
    database = Database()
    database.start()
    database.shutdown()
