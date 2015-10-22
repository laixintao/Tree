__author__ = 'laixintao'

import os
from MovieDB import create_table
from LFMSpider import LFMSpider
from config import MOVIE_DB_PATH

if __name__ == "__main__":
    if os.path.exists(MOVIE_DB_PATH):
        pass
    else:
        create_table()
    lfmspider = LFMSpider()
    lfmspider.start()

