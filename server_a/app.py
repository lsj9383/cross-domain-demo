# -*- coding:utf-8 -*-
from flask import Flask, jsonify, request, make_response
import json
import cors

app = Flask(__name__)

# 来自form标签的get跨域请求
@app.route("/get-form-cors")
def get_form_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello get form cors"
    })
    return resp

# 来自jsonp的get跨域请求
@app.route("/get-jsonp-cors")
def get_jsonp_cors():
    jsoncallback = request.args.get("callback", "jsonp_callback")
    resp = "%s(%s)" % (jsoncallback,
                    json.dumps({
                        "result" : 0,
                        "message" : "hello get form cors"
                    }))
    return resp

# ajax的get跨域请求
@app.route("/get-cors")
@cors.allower(allow_origin = "http://localhost:5001")
def get_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello get cors",
        "cookie" : str(request.cookies),
    })
    resp.set_cookie('name','lsj')
    return resp

# ajax的post跨域请求
@app.route("/post-cors", methods=["post", "OPTIONS"])
@cors.allower(
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

# ajax的get跨域请求
@app.route("/ngx-get-cors")
def ngx_get_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello ngx get cors",
        "cookie" : str(request.cookies),
    })
    resp.set_cookie('name','lsj')
    return resp

# ajax的post跨域请求
@app.route("/ngx-post-cors", methods=["post", "OPTIONS"])
def ngx_post_cors():
    resp = jsonify({
        "result" : 0,
        "message" : "hello ngx post cors",
        "cookie" : str(request.cookies),
    })
    resp.set_cookie('name','lsj')
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0")