#!/virtual/ftumn/dev/venv/bin/python3
# -*- coding: UTF-8 -*-
import sys
import cgi
import cgitb
import os
import urllib.parse

sys.path.append(os.path.join(os.path.dirname(__file__), '../../'))
from util import get_logger, cgi_debug_wrapper, default_cgi_request_header, process_cgi_request


logger = get_logger(logger_name=os.path.abspath(__file__).split("/")[-2], output_dir="./")


@cgi_debug_wrapper
def main():
    cgitb.enable()

    req_params = cgi.parse()
    page = int(req_params["page"][0])

    process_cgi_request(
        url="https://app.yaoko-app.com/flyer/1095/?page={}".format(page),
        headers=default_cgi_request_header(),
    )

    logger.info("success: keyword: {}".format(keyword))


if __name__ == '__main__':
    main()


