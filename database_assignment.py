import pymysql

conn = pymysql.connect("localhost", "root","","finalyears")
cursor = conn.cursor()

try:
    sql = """CREATE TABLE Student(
                USN int primary key, 
                Name varchar(100) not null,
                Age int
                )"""
    cursor.execute(sql)

    cursor.execute("insert into Student value(1,'Shree',23)")

except Exception as e:
    print("Exception occured.{}".format(e))

finally:
    conn.commit()
    conn.close()
