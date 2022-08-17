import pymysql.cursors
# Функция возвращает connection.
def getConnection():
    # Вы можете изменить параметры соединения.
    connection = pymysql.connect(host='192.168.0.192',
                                 user='root',
                                 password='masterkey',
                                 db='traccar',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection

def getConnection_1():
    # Вы можете изменить параметры соединения.
    connection_1 = pymysql.connect(host='127.0.0.1',
                                 user='root',
                                 password='masterkey',
                                 db='voyager',
                                 charset='utf8mb4',
                                 cursorclass=pymysql.cursors.DictCursor)
    return connection_1
