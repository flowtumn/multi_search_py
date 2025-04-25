#!/virtual/ftumn/dev/venv/bin/python3
# -*- coding: UTF-8 -*-

import sys
import os
import logging
import functools
import requests
from logging.handlers import RotatingFileHandler
import cgi
import cgitb


def get_logger(logger_name: str, output_dir: str):
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)

    handler = RotatingFileHandler(
        filename=f"{output_dir}/{logger_name}.log",
        maxBytes=10 * 1024 * 1024,
        backupCount=3,
    )

    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    handler.setFormatter(formatter)

    consoleHandler = logging.StreamHandler()
    consoleHandler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.addHandler(consoleHandler)
    return logger


def default_cgi_request_header() -> dict:
    """Requestに使用するHeaderを返します"""
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
    return headers


def process_cgi_request(url: str, headers: dict, timeout: int = 25) -> None:
    """各受け付けたcgiを処理する共通メソッド"""
    r = requests.get(
        url=url,
        headers=headers,
        timeout=25,
    )

    r.raise_for_status()

    for k, v in r.headers.items():
        print ("{}: {}".format(k, v))

    print("", flush=True) 
    sys.stdout.buffer.write(r.content)


def cgi_debug_wrapper(f):
    """fを処理時に例外が送出されたら、クライアントにエラーを返すWrapper"""

    @functools.wraps(f)
    def _invoke(*args, **kwargs):
        try:
            return f(*args, **kwargs)
        except Exception as e:
            print("Content-Type: text/html")
            print()
            print (e)

    return _invoke


