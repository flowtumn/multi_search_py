#!/virtual/ftumn/dev/venv/bin/python3
# -*- coding: UTF-8 -*-

import os
import logging
import contextlib
from logging.handlers import RotatingFileHandler
import cgi
import cgitb
import urllib.parse
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

    def _render() -> str:
        if search_type == 0:
            tp = Template(read_all("../templates/search.jinja"))
            return tp.render(
                keyword=keyword,
                checked_shopping="checked",
                checked_free_market="",
#                page1="http://www.ftumn.shop/multi_search/cgi-bin/engine/rakuten?keyword=" + keyword,
#                page2="http://www.ftumn.shop/multi_search/cgi-bin/engine/amazon?keyword=" + keyword,
#                page3="http://www.ftumn.shop/multi_search/cgi-bin/engine/yahoo?keyword=" + keyword,
#                page4="http://www.ftumn.shop/multi_search/cgi-bin/engine/kakaku?keyword=" + keyword,
                page1="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}".format(urllib.parse.quote("https://search.rakuten.co.jp/search/mall/{}".format(keyword))),
                page2="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}".format(urllib.parse.quote("https://www.maruo.co.jp/_hmas/hmas2.aspx?k={}".format(keyword))),
                page3="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}".format(urllib.parse.quote("https://shopping.yahoo.co.jp/search?p={}".format(keyword))),
                page4="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}".format(urllib.parse.quote("https://www.yodobashi.com/?word={}".format(keyword))),
            )
        elif search_type == 1:
            tp = Template(read_all("../templates/search.jinja"))
            return tp.render(
                keyword=keyword,
                checked_shopping="",
                checked_free_market="checked",
                page1="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}".format(urllib.parse.quote("https://aucfan.com/search2/q-~{}/?site=mc".format(keyword.encode("euc_jp").hex()))),
                page2="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}".format(urllib.parse.quote("https://fril.jp/s?transaction=selling&query={}".format(keyword))),
                page3="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}?open=1".format(urllib.parse.quote("https://paypayfleamarket.yahoo.co.jp/search/{}".format(keyword))),
                page4="http://www.ftumn.shop/multi_search/cgi-bin/engine/general?url={}".format(urllib.parse.quote("https://auctions.yahoo.co.jp/search/search?p={}".format(keyword))),
#                page1="https://sunbelx.com/upload/Flyer/files/e_f_1515_680ab45c-e41c-417d-ae3c-6e965583d00e.pdf",
#                page1="https://docs.google.com/viewer?url=https://sunbelx.com/upload/Flyer/files/e_f_1515_680ab45c-e41c-417d-ae3c-6e965583d00e.pdf&embedded=true",
#                page2="https://cms.mechao.tv/rogers/viewer?id=31486958&eid=65818e288ac03407f7aa82334b4c5201&sid=316a43b430d2601184ed08a42ba89a1e",
#                page3="https://cms.mechao.tv/rogers/viewer?id=31486959&eid=4866d30fcab39fad03fbace29b9fbcb8&sid=7c7baf086a80ff8fa1cd6aac0ec9eea8",
#                page4="http://www.ftumn.shop/multi_search/cgi-bin/engine/yaoko-app?page=1",
#                page5="http://www.ftumn.shop/multi_search/cgi-bin/engine/yaoko-app?page=2",
            )
        else:
            return "Unsupported search_type"

    output = _render()

    print("Content-Type: text/html")
    print()
    print (output)


if __name__ == "__main__":
    main()


