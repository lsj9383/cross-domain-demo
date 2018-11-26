# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, make_response
import json
from flask_cors import CORS

app = Flask(__name__)
# CORS(app, supports_credentials=True)

# ajax的get跨域请求
@app.route("/get-cors")
def get_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello get cors",
        "cookie" : str(request.cookies),
    })
    resp.set_cookie('name','lsj')
    resp.headers["Access-Control-Allow-Origin"] = "http://localhost:5001"
    return resp

# ajax的post跨域请求
@app.route("/post-cors", methods=["post", "OPTIONS"])
def post_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello post cors",
        "cookie" : str(request.cookies),
    })
    resp.set_cookie('name','lsj')
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0")