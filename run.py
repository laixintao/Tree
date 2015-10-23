__author__ = 'laixintao'

import os
from moviedb import create_table
from LFMSpider import LFMSpider
from config import MOVIE_DB_PATH
from log import log
from config import TIME_OUT_LOG_PATH

def parser_pages(start,end):
    try:
        log("-"*20+"RUN"+"-"*20)
        if os.path.exists(MOVIE_DB_PATH):
            pass
        else:
            create_table()
        lfmspider = LFMSpider()
        lfmspider.parser_pages(start,end,timeleg=0)
    except Exception,e:
        log(str(e))
    finally:
        log("-"*20+"END"+"-"*20)

def start_from_page1():
    parser_pages(1,617)

def parser_timeout_pages():
    log("-"*18+"TIMEOUT"+"-"*18)
    try:
        lfm = LFMSpider()
        with open(TIME_OUT_LOG_PATH) as timeout:
            for url in timeout:
                lfm.parser_one_page(turl=url)
    except Exception,e:
        log("[ERR]"+str(e))

if __name__ == "__main__":
    parser_timeout_pages()

