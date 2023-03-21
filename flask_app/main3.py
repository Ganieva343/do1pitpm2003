from main2 import app
from flask import Flask, request, current_app

@app.route('/')
def requestdata():
    return "Hello! Your IP is {} and you are using {}: ".format(request.remote_addr,
                                                                request.user_agent)
app_context = app.app_context()
app_context.push()

current_app.name
'main2'


with app.test_request_context('/products'):
     request.path  # получим полный путь к запрашиваемой странице(без домена).
     request.method
     current_app.name

'/products'
'GET'
'main2'


if __name__ == "__main__":
    app.run(debug=True)

#request.method
#Выдает ошибку
#Traceback (most recent call last):
# RuntimeError: Working outside of request context.
#
# This typically means that you attempted to use functionality that needed
# an active HTTP request. Consult the documentation on testing for
# information about how to avoid this problem.

#current_app.name
#Выдает ошибку
#Traceback (most recent call last):
#RuntimeError: Working outside of application context.

#This typically means that you attempted to use functionality that needed
#the current application. To solve this, set up an application context
#with app.app_context(). See the documentation for more information.


