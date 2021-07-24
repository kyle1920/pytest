# 必要なモジュールの取り込み
import random
import sqlite3
from flask import Flask
from datadog import initialize, statsd
from ddtrace import Pin, patch, tracer

patch(flask=True)
patch(sqlite3=True)

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

# Flaskオブジェクトの生成 --- (*1)
app = Flask(__name__)

# dbオブジェクトの生成
db = sqlite3.connect(":memory:", check_same_thread=False)

# sql文字列の初期化
sql = ""

# テーブル作成
@tracer.wrap('createTable', service='sample-app')
def createTable():

    sql = """
    create table users (
    id integer,
    name varchar(10),
    age integer
    );
    """
    db.execute(sql)

# データのインサート
@tracer.wrap('insertTable', service='sample-app')
def insertTable():

    value = random.randint(100, 10000)

    for num in range(value):
    #for num in range(5):
    #    print(str(num))
        sql = "insert into users values (" + str(num + 1) + ", 'foo', 'bar')"
        db.execute(sql)

        #   tagと値を作る
        tags = ['version:1', 'application:web']
        
        #   metricのgauge
        metric="myapp.testdata.gauge"
        statsd.gauge(metric, value, tags=tags)


# データの読み出し
@tracer.wrap('readTable', service='sample-app')
def readTable():
    c = db.cursor()
    #c.execute("select * from users where id = 1")
    c.execute("select * from users")
    #c.execute("select sum(id) from users")
    idx = 0
    for row in c:
        idx +=1
        if idx > 99994:
            print(row)

    #for row in c:
    #    print(row)

# テーブルの削除
@tracer.wrap('dropTable', service='sample-app')
def dropTable():
    sql = "drop table users"
    db.execute(sql)

# ルート( / )へアクセスがあった時の処理を記述 --- (*2)
@app.route("/")
def root():
    
    # テーブル作成
    createTable()

    # データのインサート
    insertTable()

    #データの読み出し
    readTable()

    #テーブルの削除
    dropTable()

    #   tagと値を作る
    #tags = ['version:1', 'application:web']
    #value=random.randint(0, 100)

    #   metricのset
    #metric="myapp.testdata.set"
    #statsd.set(metric, value, tags=tags)
    #   metricのgauge
    #metric="myapp.testdata.gauge"
    #statsd.gauge(metric, value, tags=tags)

    return "Hello world"

# サーバーを起動 --- (*3)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
