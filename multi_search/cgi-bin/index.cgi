#!/virtual/ftumn/dev/venv/bin/python3
# -*- coding: UTF-8 -*-

import os
import logging
import contextlib
from logging.handlers import RotatingFileHandler
import cgi
import cgitb
from jinja2 import Template
from util import cgi_debug_wrapper


def read_all(path: str) -> str:
    """pathの中身を全てreadし返します"""
    with open(path, "r", encoding='utf-8') as fp:
        return fp.read()


@cgi_debug_wrapper
def main():
    cgitb.enable()

    req_params = cgi.parse()
    search_type = int(req_params["search_type"][0])
    keyword = req_params["keyword"][0]

    tp = Template(read_all("../templates/search.jinja"))
    output = tp.render(
        keyword=keyword,
        checked_object="checked" if search_type == 0 else "",
        checked_kitchen="checked" if search_type == 1 else "",
        page1="http://www.ftumn.shop/multi_search/cgi-bin/engine/rakuten?keyword=" + keyword,
        page2="http://www.ftumn.shop/multi_search/cgi-bin/engine/amazon?keyword=" + keyword,
        page3="http://www.ftumn.shop/multi_search/cgi-bin/engine/yahoo?keyword=" + keyword,
        page4="http://www.ftumn.shop/multi_search/cgi-bin/engine/kakaku?keyword=" + keyword,
    )

    print("Content-Type: text/html")
    print()
    print (output)


if __name__ == "__main__":
    main()

