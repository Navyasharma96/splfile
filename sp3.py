import mysql.connector
m=mysql.connector.connect(host="localhost",user="navya",password="9sharma.navya",database="apurva")
cursor=m.cursor()
#s="SELECT * FROM employee WHERE age='23'"
#cursor.execute(s)
#myresult=cursor.fetchall()
#for x in myresult:
 #   print(x)
#q="SELECT * FROM employee WHERE name LIKE'%p%'"
#cursor.execute(q)
#myresult=cursor.fetchall()
#for i in myresult:
 #   print(i)
#l="SELECT * FROM employee ORDER BY name"
#cursor.execute(l)
#myresult=cursor.fetchall()
#for a in myresult:
 #   print(a)
b="DELETE FROM employee WHERE name='ramesh'"
#cursor.execute(b)
#m.commit()
#print(cursor.rowcount,"record(s) deleted")
n="SELECT * FROM employee"
cursor.execute(n)
myresult=cursor.fetchall()
for c in myresult:
    print(c)