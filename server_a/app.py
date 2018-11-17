# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, make_response
import cors

app = Flask(__name__)

@app.route("/get-form-cors")
def get_form_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello get form cors"
    })
    return resp

@app.route("/get-cors")
@cors.wrapper(allow_origin = "http://localhost:5001")
def get_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello get cors",
        "cookie" : str(request.cookies),
    })
    resp.set_cookie('name','lsj')
    return resp

@app.route("/post-cors", methods=["post", "OPTIONS"])
@cors.wrapper(
    allow_origin = "*",
    allow_headers = "content-type")
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