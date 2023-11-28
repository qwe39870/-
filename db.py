import pymysql

def getcon():

    return pymysql.connect(host='localhost',user='root',password='0106',database="pill",charset='utf8')

def querydata(sql):
    conn=getcon()
    try:
        cusor=conn.cursor(pymysql.cursors.DictCursor)
        cusor.execute(sql)
        return cusor.fetchall()
    
    finally:
        conn.close()



if __name__ == "__main__":
    sql="select * from newtest_test"
    datas=querydata(sql)
    # for data in datas:
    #     print(data['name'])
    import pprint
    pprint.pprint(datas['name'])

