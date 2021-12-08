from flask import Flask, render_template, request, render_template_string, url_for, redirect
from jinja2 import Template
import sqlite3, logging

app = Flask(__name__)

#from contrast.flask import ContrastMiddleware
#app.wsgi_app = ContrastMiddleware(app)

# dbオブジェクトの生成
db = sqlite3.connect(":memory:", check_same_thread=False)

# sql文字列の初期化
sql = ""

# テーブル作成
def createTable():

	cur = db.cursor()

	# テーブルの存在の確認
	sql = "select count(*) FROM sqlite_master WHERE TYPE='table' AND name='users'"

	cur.execute(sql)
	isTblExist = cur.fetchone()

	print("isTblExist:" + str(isTblExist[0]))

	if isTblExist[0] == 0:

		sql = """
		create table users (
		id integer,
		name varchar(10),
		age integer
		);
		"""
		db.execute(sql)

# テーブルにインサート
def insertTable(strID, strName, strAge):

	sql = "insert into users values ('" + strID + "', '" + strName + "', '" + strAge + "')"
	db.execute(sql)

# テーブルから行の取得
def selectTable(strID):

	if strID == "":

		sql = "select * from users"

	else:

		sql = "select * from users where strID = '" + strID + "'"

	
	for a in db.execute(sql):
		print(a)




# getのときの処理
@app.route('/', methods=['GET'])
def index():

	createTable()

	return render_template('index.html', \
		title = 'Python Flask Sample', \
		message = '以下を入力して下さい。')

# postのときの処理	
@app.route('/', methods=['POST'])
def post():
	id = request.form['id']
	name = request.form['name']
	age = request.form['age']

	insertTable(id, name, age)

	return redirect(url_for('saved', name=name))

@app.route('/saved')
def saved():
	return render_template('index2.html', \
		title = 'Python Flask Sample', \
		message = request.args.get('name') + ' さんのデータが挿入されました。')


@app.route('/user')



@app.route('/user/<id>')



@app.route('/echo', methods=['GET'])
def echo():
    return render_template_string(request.args.get('q', ''))



if __name__ == "__main__":
    app.run(debug=True, host='192.168.1.222', port=8888, threaded=True)
