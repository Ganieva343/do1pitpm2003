from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    print(i)
    return 'Hello World'


@app.route('/one')
def indexone():
    return 'Home Page'


@app.route('/contact/')
@app.route('/career/')
def career():
    return 'Career Page'


@app.route('/feedback/')
def feedback():
    return 'Feedback Page'


def indexo():
    return 'Hello'


app.add_url_rule('/o', 'indexo', indexo)


@app.route('/user//')
def user_profile(id):
    return "Profile page of user #{}".format(id)


if __name__ == "__main__":
    app.run(debug=True)