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
        self.ispost = False
        # self.movies = []
        self.isp = False
        self.istitle = False
        # self.num_movie = 0
        # self.have_pic = False
        self.pic = ""
        self.hasurl = False
        self.url = ""
        self.title = ""
        self.ch_sent=""
        self.en_sent=""
        self.movie=""
        self.line = 0

    def show_data(self):
        print "title:",self.title
        print "url:",self.url
        print "movie:",self.movie
        print "pic:",self.pic
        print "ch:",self.ch_sent
        print "en:",self.en_sent
        print("-"*20)



    def handle_data(self, data):
        if self.isp:
            # print self.line,data
            if len(data)>4:
                if self.line==0:
                    self.ch_sent = data
                    # self.line += 1
                elif self.line == 1:
                    self.en_sent = data
                elif self.line == 2:
                    self.movie = data
                self.line += 1
            else:
                # print "*"*20,data
                pass
        if self.istitle:
            self.title = data
        else:
            pass

    def handle_starttag(self, tag, attrs):
        if tag == "h1" and attrs[0][1]=="entry-title":
            self.ispost = True
            self.istitle = True
        # if tag == "div" and attrs[0][1] == "entry-content":
        #     self.line += 1
        if tag == "p":
            self.isp = True
        if tag == "img":
            if self.isp:
                self.pic=attrs[1][1]
                self.have_pic = True
        if tag == "a" and self.istitle:
            self.url = attrs[0][1]
            self.hasurl = True


    def handle_endtag(self, tag):
        if tag == "p":
            self.isp = False
            # self.have_pic = False
        if tag == "article":
            self.show_data()
            self.line = 0;
            self.ispost = False

        if tag == "h1":
            self.istitle = False

    def handle_charref(self,name):
        try:
            charnum=int(name)
        except ValueError:
            return
        if charnum<1 or charnum>255:
            return
        self.handle_data(chr(charnum))

class LFMspider(object):
    "spider on lessonsfrommocies"
    limit_url = "http://lessonsfrommovies.net/"
    start_url = limit_url
    movies = []

    def start(self):
        html_page = urllib2.urlopen(
            self.start_url).read()
        # print html_page
        # self.on_every_page(html_page)
        begin = MovieHtmlParser()
        html = begin.unescape(html_page)
        begin.feed(html)
        # begin.show_data()
        # for pc in begin.pic:
        #     print pc
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