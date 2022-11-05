from flask import render_template, Flask


app = Flask(__name__)


@app.route('/users')
def hello():
    return render_template('index.html')


@app.route('/users/5')
def users():
    return render_template('users/show.html', name=5)


if __name__ == '__main__':
    app.run()
