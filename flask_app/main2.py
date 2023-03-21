from flask import Flask


app = Flask(__name__)


@app.route('/H')
def index():
    return 'Hello Flask'


@app.route('/user//')
def user_profile(user_id):
    return "Profile page of user #{}".format(user_id)


@app.route('/books//')
def books(genre):
    return "All Books in {} category".format(genre)


if __name__ == "__main__":
    app.run(debug=True)