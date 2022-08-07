# import mysql.connector
import pymysql
try:
    connection = pymysql.connect(host='localhost',
                                         database='onlinewebsite',
                                         user='root',
                                         password='')

    sql_select_Query = "select * from cart"
    cursor = connection.cursor()
    cursor.execute(sql_select_Query)
    # get all records
    records = cursor.fetchall()
    print("Total number of rows in table: ", cursor.rowcount)

    print("\nPrinting each row")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("Title  = ", row[2])
        print("Price  = ", row[3], "\n")

except pymysql.Error as e:
    print("Error reading data from MySQL table", e)
finally:
    if connection.is_connected():
        connection.close()
        cursor.close()
        print("MySQL connection is closed")
