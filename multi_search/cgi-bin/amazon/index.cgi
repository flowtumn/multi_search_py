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
    url="https://www.amazon.co.jp/s/k={}".format(keyword),
    headers={
        e[5:].replace("_", "-"): v
        for e, v in os.environ.items()
        if e in [
            "HTTP_USER_AGENT",
            "HTTP_ACCEPT",
            "HTTP_ACCEPT_ENCODING",
            "HTTP_ACCEPT_LANGUAGE",
            "HTTP_COOKIE",
            "HTTP_CONNECTION",
            "HTTP_UPGRADE_INSECURE_REQUESTS",
            "HTTP_REFERER",
            "HTTP_PRAGMA", 
            "HTTP_CACHE_CONTROL",
        ]
    },
    timeout=10,
)

r = requests.get(
    url="https://www.amazon.co.jp/s/k={}".format(keyword),
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    },
    timeout=10,
)

for k, v in r.headers.items():
    print ("{}: {}".format(k, v))

print()
#print (r.text)
print (r.status_code)
print({
        e[5:].replace("_", "-"): v
        for e, v in os.environ.items()
        if e in [
            "HTTP_USER_AGENT",
            "HTTP_ACCEPT",
            "HTTP_ACCEPT_ENCODING",
            "HTTP_ACCEPT_LANGUAGE",
            "HTTP_COOKIE",
            "HTTP_CONNECTION",
            "HTTP_UPGRADE_INSECURE_REQUESTS",
            "HTTP_REFERER",
            "HTTP_PRAGMA", 
            "HTTP_CACHE_CONTROL",
        ]
    }
)
