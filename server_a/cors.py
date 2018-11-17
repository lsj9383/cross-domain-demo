# -*- coding:utf-8 -*-
from flask import request, make_response

import functools

__cors_response_headers_allow_origin__ = "Access-Control-Allow-Origin"
__cors_response_headers_allow_headers__ = "Access-Control-Allow-Headers"

def wrapper(allow_origin = None, allow_headers = None):
    def deractor(f):
        @functools.wraps(f)
        def inner(*ks, **kws):
            if request.method == "OPTIONS":
                resp = make_response()
                if allow_origin is not None:
                    resp.headers[__cors_response_headers_allow_origin__] = allow_origin
                if allow_headers is not None:
                    resp.headers[__cors_response_headers_allow_headers__] = allow_headers
                resp.headers["Access-Control-Allow-Credentials"] = "true"
                return resp
            rv = f(*ks, **kws)
            if isinstance(rv, str):
                rv = make_response(rv)
            if allow_origin is not None:
                rv.headers[__cors_response_headers_allow_origin__] = allow_origin
            rv.headers["Access-Control-Allow-Credentials"] = "true"
            return rv
        return inner
    return deractor