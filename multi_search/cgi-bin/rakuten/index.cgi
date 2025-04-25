#!/virtual/ftumn/dev/venv/bin/python3
# -*- coding: UTF-8 -*-
import sys
import cgi
import cgitb
import requests
import os
import urllib.parse
import logging
from logging.handlers import RotatingFileHandler


cgitb.enable()

def main():
    req_params = cgi.parse()
    keyword = req_params["keyword"][0]

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
    }
    headers["Accept-Encoding"] = ""

    r = requests.get(
        url="https://search.rakuten.co.jp/search/mall/{}".format(urllib.parse.quote(keyword)),
        headers=headers,
        timeout=25,
    )

    for k, v in r.headers.items():
        print ("{}: {}".format(k, v))

    print("", flush=True) 
    sys.stdout.buffer.write(r.content)

try:
    main()
except Exception as e:
    print("Content-Type: text/html")
    print()
    print (e)

