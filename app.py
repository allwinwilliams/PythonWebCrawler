import os
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"

@app.route('/test',methods=['GET'])
def test_func():
    return jsonify("Hello, World!")

@app.route('/request',methods=['GET'])
def request_func():
    x = request.args.get('q')
    return jsonify("query",x)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
