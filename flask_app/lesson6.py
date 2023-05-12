from flask import Flask, request, render_template
from jinja2 import Template


t = Template("Name: {{ name }}")
t.render(name='Jerry')
'Name: Jerry'

app = Flask(__name__)

@app.route('/')
def index():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)


@app.route('/2')
def index2():
    return render_template('index2.html')


if __name__ == "__main__":
    app.run()