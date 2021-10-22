from flask import Flask, render_template, request, render_template_string

app = Flask(__name__)

from contrast.flask import ContrastMiddleware
app.wsgi_app = ContrastMiddleware(app)

# getのときの処理
@app.route('/', methods=['GET'])
def get():
	return render_template('index.html', \
		title = 'Form Sample(get)', \
		message = '名前を入力して下さい。')

# postのときの処理	
@app.route('/', methods=['POST'])
def post():
	name = request.form['name']

	#return render_template('index.html', \
	#	title = 'Form Sample(post)', \
	#	message = 'こんにちは、{}さん'.format(name))

        vln = render_template(name)
        return vln.renmder()

@app.route('/echo', methods=['GET'])
def echo():
    return render_template_string(request.args.get('q', ''))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8888, threaded=True)
