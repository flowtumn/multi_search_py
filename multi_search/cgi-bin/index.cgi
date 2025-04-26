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

    def _render():
        if search_type == 0:
            output = tp.render(
                keyword=keyword,
                checked_object="checked",
                checked_kitchen="",
                page1="http://www.ftumn.shop/multi_search/cgi-bin/engine/rakuten?keyword=" + keyword,
                page2="http://www.ftumn.shop/multi_search/cgi-bin/engine/amazon?keyword=" + keyword,
                page3="http://www.ftumn.shop/multi_search/cgi-bin/engine/yahoo?keyword=" + keyword,
                page4="http://www.ftumn.shop/multi_search/cgi-bin/engine/kakaku?keyword=" + keyword,
            )
        elif search_type == 1:
            output = tp.render(
                keyword=keyword,
                checked_object="",
                checked_kitchen="checked",
                page1="https://sunbelx.com/upload/Flyer/files/e_f_1515_680ab45c-e41c-417d-ae3c-6e965583d00e.pdf",
                page2="http://www.ftumn.shop/multi_search/cgi-bin/engine/yaoko-app?keyword=" + keyword,
                page3="https://cms.mechao.tv/rogers/viewer?id=31486958&eid=65818e288ac03407f7aa82334b4c5201&sid=316a43b430d2601184ed08a42ba89a1e",
                page4="https://cms.mechao.tv/rogers/viewer?id=31486959&eid=4866d30fcab39fad03fbace29b9fbcb8&sid=7c7baf086a80ff8fa1cd6aac0ec9eea8",
            )
        else:
            return "Unsupported search_type"

    output = _render()

    print("Content-Type: text/html")
    print()
    print (output)


if __name__ == "__main__":
    main()

