from datadog import initialize, statsd
from ddtrace import Pin, patch
patch(flask=True)

#options = {
#    'statsd_host':'127.0.0.1',
#    'statsd_port':8125
#}

#initialize(**options)

# 必要なモジュールの取り込み
from flask import Flask

# Flaskオブジェクトの生成 --- (*1)
app = Flask(__name__)

# ルート( / )へアクセスがあった時の処理を記述 --- (*2)
@app.route("/")
def root():
    import test02.py

    return "Hello"

    #   tagと値を作る
    #tags = ['version:1', 'application:web']
    #value=random.randint(0, 100)

    #   metricのset
    #metric="myapp.testdata.set"
    #statsd.set(metric, value, tags=tags)
    #   metricのgauge
    #metric="myapp.testdata.gauge"
    #statsd.gauge(metric, value, tags=tags)

# サーバーを起動 --- (*3)
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888)
