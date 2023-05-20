from flask import Flask,  render_template


app = Flask(__name__, template_folder='templates')


@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/dote')
def index2():
    return render_template('dote.html')


@app.route('/home')
def home():
    return "Это домашняя страница"


@app.route('/blog')
def blog():
    return "Это мой блог"


@app.route('/cont')
def contact():
    return "Ты на странице 'Contact'"


if __name__ == "__main__":
    app.run(debug=True)