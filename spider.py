#!/user/bin/env python
#_*_ coding: utf-8 _*_

__author__="laixintao"

import urllib2
import re
from movie import Movie
from HTMLParser import HTMLParser

# set the system encoding
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)


class PageFormatError(BaseException):
    pass

# don't need a standalone data structure
# just use movie
# class Item():
#     "data structure"
#     sent_ch = ""
#     sent_en = ""
#     pic = ""
#     movie = ""
#     url = ""

class MovieHtmlParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []
        self.isp = False
        self.num_movie = 0

    def handle_data(self, data):
        if self.isp:
            print self.num_movie,data
        else:
            pass

    def handle_starttag(self, tag, attrs):
        if tag == "div" and attrs[0][1] == "entry-content":
            self.num_movie += 1
        if tag == "p":
            self.isp = True

    def handle_endtag(self, tag):
        if tag == "p":
            self.isp = False

class LFMspider(object):
    "spider on lessonsfrommocies"
    limit_url = "http://lessonsfrommovies.net/"
    start_url = limit_url
    movies = []

    def start(self):
        html_page = urllib2.urlopen(self.start_url).read()
        # print html_page
        # self.on_every_page(html_page)
        begin = MovieHtmlParser()
        begin.feed(html_page)
        begin.close()

    def on_every_page(self,html):
        num_post = 3 #3 post on each page
        entry_content = re.compile(
            r'entry.content[\s\S]*?\.entry.content')
            # r"<p>[\s\S]*?</p>")
        p = re.compile(r"<p>[\s\S]*?</p>")
        each = entry_content.findall(html)
        # for i in each:
            # print "---------"
            # movie = Movie()
            # ps = p.findall(i)
            # for ii in ps:
            #     print ii
        return each

if __name__ == "__main__":
    print "ss"