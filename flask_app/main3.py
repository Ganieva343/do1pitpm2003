from main2 import app
from flask import Flask, request, current_app

app_context = app.app_context()
app_context.push()

current_app.name


with app.test_request_context('/products'):
     request.path  # получим полный путь к запрашиваемой странице(без домена).
     request.method
     current_app.name


'/products'
'GET'
'main2'