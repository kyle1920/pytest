import sqlite3

db = sqlite3.connect(":memory:")
sql = """
create table users (
  id integer,
  name varchar(10),
  age integer
);
"""
db.execute(sql)
for num in range(1000):
#for num in range(5):
    print(str(num))
    sql = "insert into users values (" + str(num + 1) + ", 'foo', 'bar')"
    db.execute(sql)
c = db.cursor()
#c.execute("select * from users where id = 1")
c.execute("select * from users")
idx = 0
for row in c:
   idx +=1
   if idx > 994:
        print(row)