import conn_db
import pymysql.cursors   
import rw_c
global last_id
last_id = rw_c.last_id

# Подключиться к базе данных.
# Используется конфигурация подключений из conn_db
'''
connection = pymysql.connect(host='192.168.0.192',
                             user='root',
                             password='masterkey',                             
                             db='traccar',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
'''
connection = conn_db.getConnection()
print ("connect traccar successful!!")

connection_1 = conn_db.getConnection_1()
print ("connect georitm voyager successful!!")

try:  
    with connection.cursor() as cursor: 
        # SQL 
        #sql = "SELECT * FROM tc_positions WHERE ID=56987"
        #sql_obj = "SELECT * FROM tc_devices where id=7"
        #pos = sql_obj['positionid']
        sql = f"""SELECT * FROM tc_positions WHERE ID > {last_id}"""
        #lat = sql[0]['latitude']
        #lon = sql[0]['longitude']
        # Выполнить команду запроса (Execute Query).
        cursor.execute(sql) 
        #print ("cursor.description: ", cursor.description)
        #print(pos)
        for row in cursor:
            lat = row['latitude']
            lon = row['longitude']
            #Записываю ID последней записи чтобы в дальнейшем начинать с нее
            id_c = row['id']
            last_idw = f"""last_id = {id_c}"""
            file = open("rw_c.py", "w")
            file.write(last_idw)
            file.close()
            #преобразуем координаты в формат георитм
            degrees_lat = int(lat)
            temp = 60 * (lat - degrees_lat)
            minutes_lat = int(temp)
            #seconds = 60 * (temp - minutes)
            seconds_lat = str(temp - minutes_lat)
            sp_lat = (seconds_lat.split("."))
            sp1_lat = sp_lat[1]
            #print(degrees, minutes, seconds)
            lat_g = round(float(f"""{degrees_lat}{minutes_lat}.{sp1_lat}  """), 6)

            degrees_lon = int(lon)
            temp = 60 * (lon - degrees_lon)
            minutes_lon = int(temp)
            #seconds = 60 * (temp - minutes)
            seconds_lon = str(temp - minutes_lon)
            sp_lon = (seconds_lon.split("."))
            sp1_lon = sp_lon[1]
            #print(degrees, minutes, seconds)
            lon_g = round(float(f"""{degrees_lon}{minutes_lon}.{sp1_lon}  """), 6)
            # Отсюда надо передать полученные данные в базу вояджер
            print(lat_g, lon_g)
#-----------------------------------------------------------------------------------
'''
Полученные lat_g и lon_g ну и ряд других переменных пока не выделенных надо передать в базу voyager посредством:
сюда только самую свежую точку
UPDATE voyager.obj SET lat='5215.39504', lon='10421.67392', point_date='2022-08-15 00:01:00', d_online='2022-08-15 00:01:00', S30='REV 07.502.155', local_rid=1, remote_rid=1, I10=400  WHERE ID=50;
сюда все поступившие
INSERT INTO voyager.records (id_obj, rec_date, rid, rec_type, lat, lon, spd, power, d1, d2, d3, d4, d5, d6, an1, an2, car_power) VALUES (50, '2022-08-16 04:51:34', 1, 1, 5538.71, 10919.5046, 5.2, 1, 1, 1, 1, 1, 1, 1, 555, 777, 1320);
И весь скрипт должен как то работать в цикле передавая данные по мере поступления

https://betacode.net/11463/connect-to-mysql-database-in-python-using-pymysql

# пример UPDATE
import myconnutils
import pymysql.cursors
import datetime

connection = myconnutils.getConnection()
print ("Connect successful!")
try :
    cursor = connection.cursor()
    sql = "Update Employee set Salary = %s, Hire_Date = %s where Emp_Id = %s "
    # Hire_Date
    newHireDate = datetime.date(2002, 10, 11)
    # Выполнить sql и передать 3 параметра.
    # ​​​​​​​
    rowCount = cursor.execute(sql, (850, newHireDate, 7369 ) )
    connection.commit()
    print ("Updated! ", rowCount, " rows")
finally:
    # Закрыть соединение
    connection.close()


'''

            #print(row)
            #print(lat, lon)
finally:
    # Закрыть соединение (Close connection).      
    connection.close()
