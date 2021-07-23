from datadog import initialize, statsd

options = {
    'statsd_host':'127.0.0.1',
    'statsd_port':8125
}

initialize(**options)

# 必要なモジュールの取り込み
from flask import Flask

# Flaskオブジェクトの生成 --- (*1)
app = Flask(__name__)

# ルート( / )へアクセスがあった時の処理を記述 --- (*2)
@app.route("/")
def root():
    return "Hello"

# サーバーを起動 --- (*3)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
