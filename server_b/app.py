# -*- coding:utf-8 -*-
from flask import Flask, make_response
from flask_cors import CORS

app = Flask(__name__)

@app.route("/cookie")
def gen_cookie():
    resp = make_response("hello cookie")
    resp.set_cookie('sex','man')
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)