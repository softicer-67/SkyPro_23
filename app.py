from flask import render_template, request, Flask


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/main/index.html', title='Главная')


@app.route('/users')
def get_users():
    users = ['mike', 'mishel', 'adel', 'keks', 'kamila']
    arg = request.args.get('arg')
    if not arg:
        arg = ''
    flt_users = filter(lambda x: arg in x, users)
    return render_template('/users/users.html', users=flt_users, search=arg)


@app.route('/users/<id>')
def users_id(id):
    return render_template('/users/show.html', title='about the user', name=id)


if __name__ == "__main__":
    app.run(debug=True)
