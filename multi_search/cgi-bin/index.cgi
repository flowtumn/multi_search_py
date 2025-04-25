#!/virtual/ftumn/dev/venv/bin/python3
# -*- coding: UTF-8 -*-

import os
import cgi
import cgitb
from jinja2 import Template


cgitb.enable()

req_params = cgi.parse()
search_type = int(req_params["search_type"][0])
keyword = req_params["keyword"][0]

def read_all(path: str) -> str:
    with open(path, "r", encoding='utf-8') as fp:
        return fp.read()


tp = Template(read_all("../templates/search.jinja"))
output = tp.render(
    keyword=keyword,
    checked_object="checked" if search_type == 0 else "",
    checked_kitchen="checked" if search_type == 1 else "",
    page1="http://www.ftumn.shop/multi_search/cgi-bin/rakuten?keyword=" + keyword,
    page2="http://www.ftumn.shop/multi_search/cgi-bin/amazon?keyword=" + keyword,
    page3="http://www.ftumn.shop/multi_search/cgi-bin/yahoo?keyword=" + keyword,
    page4="http://www.ftumn.shop/multi_search/cgi-bin/kakaku?keyword=" + keyword,
)

print("Content-Type: text/html")
print()
print (output)
