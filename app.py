from flask import render_template, Flask, request


app = Flask(__name__)


@app.route('/')
def index_():
    return 'Главная страница'


@app.route('/users')
def users_():
    users_list = ['mike', 'mishel', 'adel', 'keks', 'kamila']
    term = request.args.get('term')
    users = filter(lambda x: term in x, users_list)
    return render_template('users/second_file.html', users=users, search=term)


@app.route('/users/<id>')
def users_id(id):
    return render_template('users/index.html', id=id)


if __name__ == '__main__':
    app.run()
