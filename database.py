import pymysql
 
con = None 
cur = None
def dbconnect():
    global con,cur
    try: 
        con = pymysql.connect(host= 'localhost',
                            database = 'onlinewebsite',
                            user = 'root',
                            password = '')
        cur = con.cursor()
    except Exception as e:
        print(e)

def dbdisconnect():
    con.close()

def readrecord():
    dbconnect()
    query = 'select * from cart'
    cur.execute(query)
    records = cur.fetchall()
    dbdisconnect()
    return records

def readimagebyid(id):
    dbconnect()
    query = f"select * from cart where idcart={id}"
    cur.execute(query)
    records = cur.fetchall()
    dbdisconnect()
    return records


