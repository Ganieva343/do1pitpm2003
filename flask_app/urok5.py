
from flask import Flask, make_response, redirect


app = Flask(__name__)


@app.route('/book/<string:genre>')
def books(genre):
    res = make_response({"message": "All Books in {} category".format(genre)}, 200)
    res.headers['Content-Type'] = 'text/plain'
    res.headers['Server'] = 'pythonProject1'
    return res


@app.route('/')
def http_404_handler():
    return make_response("404 Error", 400)


@app.route('/set-cookie')
def set_cookie():
    res = make_response("Cookie setter")
    res.set_cookie("favorite-color", "skyblue", 60*60*24*15)
    res.set_cookie("favorite-font", "sans-serif", 60*60*24*15)
    return res


@app.route('/cort')
def http_500_handler():
    return "500 Error", 500


@app.route('/corte')
def render_markdown():
    return "## Heading", 200, {'Content-Type': 'text/markdown'}


@app.route('/transfer')
def transfer():
    return "", 302, {'location': 'https://localhost:5000/login'}

@app.route('/transfere')
def transfere():
    return redirect("https://localhost:5000/login")


@app.route('/transferer')
def transferer():
    return redirect("https://localhost:5000/login", code=301)


if __name__ == "__main__":
    app.run(debug=True)