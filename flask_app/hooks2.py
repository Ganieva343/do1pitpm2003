from flask import Flask, request, g, abort

app = Flask(__name__)


@app.errorhandler(404)
def http_404_handler(error):
    return "HTTP 404 Error Encountered", 404

@app.errorhandler(500)
def http_500_handler(error):
    return "HTTP 500 Error Encountered", 500

@app.route("/")
def index():
    # print("index() called")
    # return 'Testings Request Hooks'
    abort(404)

if __name__ == "__main__":
    app.run(debug=True)