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
    sql = "insert into users values (" + str(num) + ", 'foo', 'bar')"
    db.execute(sql)
c = db.cursor()
c.execute("select * from users where id = 1")
for row in c:
    if row > 995:
        print(row) 