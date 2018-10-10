import pymysql

db = pymysql.connect(host='localhost', port=3306, user='root', password='wjw123456',charset='utf8mb4')
cursor = db.cursor(cursor=pymysql.cursors.DictCursor) # 查询返回结果是以字典形式
cursor.execute('SELECT VERSION()')
data = cursor.fetchone()    # 获取第一条数据
print('Database Version:', data)

#region 建数据库
cursor.execute('CREATE DATABASE IF NOT EXISTS spiders DEFAULT CHARACTER SET utf8mb4' )
cursor.execute('USE spiders')
#endregion

#region 建表
sql = 'CREATE TABLE IF NOT EXISTS students(id VARCHAR(255) NOT NULL, name VARCHAR(255) NOT NULL, age INT NOT NULL, PRIMARY KEY (id))'
cursor.execute(sql)
#endregion

#region 通用的插入数据方法，数据存在则修改数据，不存在则插入数据
data = {
    'id': '20120002',
    'name': 'Bob王',
    'age': 28
}
tablename = 'students'
keys = ', '.join(data.keys())
values = ', '.join(['%s'] * len(data))
sql = 'INSERT INTO {table}({keys}) values({values}) ON DUPLICATE KEY UPDATE'\
        .format(table=tablename, keys=keys, values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data]) # 遍历得到键名
sql += update

print(sql)
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('successful')
        db.commit()
except Exception as ex:
    print('failure: ', ex)
    db.rollback()

#endregion

#region update
# sql = 'UPDATE students SET age = %s WHERE name = %s'
# try:
#     cursor.execute(sql, (25, 'Bob'))
#     db.commit()
# finally:
#     db.rollback()
#endregion

#region delete
# table = 'students'
# condition = 'age > 25'
# sql = 'DELETE FROM  {table} WHERE {condition}'.format(table=table, condition=condition)
# try:
#     cursor.execute(sql)
#     db.commit()
# except:
#     db.rollback()
#endregion

#region 查询语句
sql = 'SELECT * FROM students WHERE age >= 20'
 
try:
    cursor.execute(sql)
    print('Count:', cursor.rowcount)
    one = cursor.fetchone()
    print('One:', one)
    results = cursor.fetchall()
    print('Results:', results)
    print('Results Type:', type(results))
    for row in results:
        print(row)
    
    print('-' * 100)
    cursor.scroll(0,mode='absolute')  #相对绝对位置移动
    row = cursor.fetchone()
    while row:
        print('Row:', row)
        row = cursor.fetchone()
except:
    print('Error')
#endregion

db.close()