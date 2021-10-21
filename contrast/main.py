from flask import *

app = Flask(__name__)


# postのときの処理	
@app.route('/', methods=['POST'])
def post():
	memo = request.form['memo']
	return render_template('index.html',
    message = '入力された内容は{}です'.format(memo))


@app.route("/<name>", methods=["GET", "POST"])
def namepage(name):
    return render_template("name.html")


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
