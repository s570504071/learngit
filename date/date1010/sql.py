#-*-coding:utf-8-*-
import MySQLdb
#注意：密码需要时passwd，如果password会报错！！
#db表示数据库testdb，use_unicode=True和charset='utf8'应该一样吧，注意不是utf-8
try:
    conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='password',port=3306,charset='utf8',db='testdb')
except Exception:
    cur=conn.cursor()
    cur.execute("create table family(name VARCHAR(20),age VARCHAR(20))")
    #插入多组数据用executemany，一般则是用execute
    cur.executemany('insert into family values(%s,%s)',[('lin',22),('qiao',23),('wu',50),('pan',52)])
    cur.close()
    conn.commit()
    conn.close()
    print 'something is a wrong'
finally:
    cur=conn.cursor()
    cur.execute('select * from family')
    #查看数据时用fetchall
    family_info=cur.fetchall()
    for name,age in family_info:
        print 'name:{name},age:{age}'.format(name=name,age=age)
    #用完记得关闭
    cur.close()
    conn.close()
    print 'done'