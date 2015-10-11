__author__ = 'laixintao'

import os
from movie import create_table
from spider import LFMspider

if __name__ == "__main__":
    if os.path.exists("movie.db"):
        pass
    else:
        create_table()

    lfmspider = LFMspider()
    lfmspider.start()