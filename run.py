__author__ = 'laixintao'

import os
from moviedb import create_table
from LFMSpider import LFMSpider
from config import MOVIE_DB_PATH
from log import log

if __name__ == "__main__":
    try:
        log("-"*20+"RUN"+"-"*20)
        if os.path.exists(MOVIE_DB_PATH):
            pass
        else:
            create_table()
        lfmspider = LFMSpider()
        lfmspider.parser_pages(309,600)
    except Exception,e:
        log(str(e))
    finally:
        log("-"*20+"END"+"-"*20)

