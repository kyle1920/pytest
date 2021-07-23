import sqlite3
from ddtrace import Pin, patch


patch(sqlite3=True)

db = sqlite3.connect(":memory:")
sql = """
create table users (
id integer,
name varchar(10),
age integer
);
"""
db.execute(sql)

for num in range(10000):
#for num in range(5):
#    print(str(num))
    sql = "insert into users values (" + str(num + 1) + ", 'foo', 'bar')"
    db.execute(sql)
c = db.cursor()
#c.execute("select * from users where id = 1")
c.execute("select * from users")
#c.execute("select sum(id) from users")
idx = 0
for row in c:
    idx +=1
    if idx > 9994:
        print(row)
#for row in c:
#    print(row)