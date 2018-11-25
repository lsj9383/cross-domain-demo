# -*- coding:utf-8 -*-
from flask import request, make_response

import functools

__cors_headers_allow_origin__ = "Access-Control-Allow-Origin"
__cors_headers_allow_headers__ = "Access-Control-Allow-Headers"
__cors_headers_allow_methods__ = "Access-Control-Allow-Methods"
__cors_headers_expose_headers__ = "Access-Control-Expose-Headers"
__cors_headers_max_age__ = "Access-Control-Max-Age"
__cors_headers_allow_cred__ = "Access-Control-Allow-Credentials"

def __set_resp_header__(response, header, value):
    if value is not None:
        response.headers[header] = value

def allower(*,
        allow_origin = None,
        allow_headers = None,
        allow_methods = None,
        expose_headers = None,
        options_max_age = None,
        allow_cred = None
        ):
    def deractor(f):
        @functools.wraps(f)
        def inner(*ks, **kws):
            if request.method == "OPTIONS":
                resp = make_response()
                __set_resp_header__(resp, __cors_headers_allow_origin__, allow_origin)
                __set_resp_header__(resp, __cors_headers_allow_headers__, allow_headers)
                __set_resp_header__(resp, __cors_headers_allow_methods__, allow_methods)
                __set_resp_header__(resp, __cors_headers_expose_headers__, expose_headers)
                __set_resp_header__(resp, __cors_headers_max_age__, options_max_age)
                __set_resp_header__(resp, __cors_headers_allow_cred__, allow_cred)
                return resp
            resp = f(*ks, **kws)
            if isinstance(resp, str):
                resp = make_response(rv)
            __set_resp_header__(resp, __cors_headers_allow_origin__, allow_origin)
            __set_resp_header__(resp, __cors_headers_allow_cred__, allow_cred)
            return resp
        return inner
    return deractor
