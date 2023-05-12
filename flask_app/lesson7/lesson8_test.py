from lesson8 import app
from flask import url_for

with app.test_request_context('/'):
    print(url_for('index'))

with app.test_request_context('/'):
    print(url_for('index', _external=True))

with app.test_request_context('/'):
    print(url_for('books', genre='biography', page=2, sort_by='date-published'))