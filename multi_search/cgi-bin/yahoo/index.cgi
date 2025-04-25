#!/virtual/ftumn/dev/venv/bin/python3
# -*- coding: UTF-8 -*-
import cgi
import cgitb
import math
import json
import requests
import os


cgitb.enable()


req_params = cgi.parse()
keyword = req_params["keyword"][0]


r = requests.get(
    url="https://shopping.yahoo.co.jp/search?p={}".format(keyword),
    headers={
        e[5:]: v
        for e, v in os.environ.items()
        if e in [
            "HTTP_USER_AGENT",
            "HTTP_ACCEPT",
            "HTTP_ACCEPT_ENCODING",
            "HTTP_ACCEPT_LANGUAGE",
            "HTTP_COOKIE",
        ]
    },
    timeout=10,
)

for k, v in r.headers.items():
    print ("{}: {}".format(k, v))

print()
print (r.text)
