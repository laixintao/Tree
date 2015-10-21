__author__ = 'laixintao'

import os
from MovieDB import create_table
from spider import LFMspider
from config import MOVIE_DB_PATH

if __name__ == "__main__":
    if os.path.exists(MOVIE_DB_PATH):
        pass
    else:
        create_table()

    lfmspider = LFMspider()
    with open()
    try:
        lfmspider.start()
