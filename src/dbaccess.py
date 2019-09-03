import configparser, mysql.connector



def db_access():
    config = configparser.ConfigParser()
    config.read("src/db.config")
    print (config.get("DB", "host"))
    return mysql.connector.connect(
                host=config.get("DB", "host"),
                user=config.get("DB", "user"),
                passwd=config.get("DB", "passwd"))


db_access()