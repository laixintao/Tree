#!/user/bin/env python
#_*_ coding: utf-8 _*_

__author__="laixintao"

import urllib2
import re
import time
from moviedb import Movie,DBSession
from HTMLParser import HTMLParser
from log import log

# set the system encoding
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)

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
        self.next_page_url = ""

    def get_next_page_url(self):
        return self.next_page_url

    def clear_next_page_url(self):
        self.next_page_url = None

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
                else :pass
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
        if tag == "p":
            self.isp = True
        if tag == "img":
            if self.isp:
                self.pic=attrs[1][1]
                self.have_pic = True
        if tag == "a" and self.istitle:
            self.url = attrs[0][1]
            self.hasurl = True
            self.id = re.findall(r"[\d]{1,5}",self.url)[0]


    def handle_endtag(self, tag):
        if tag == "p":
            self.isp = False
            # self.have_pic = False
        if tag == "article":
            # self.show_data()
            self.add_to_db()
            self.line = 0;
            self.ispost = False
        if tag == "h1":
            self.istitle = False

    def add_to_db(self):
        try:
            s = DBSession()
            old = s.query(Movie).filter(Movie.url==self.url).first()
            if old == None:
            # if True:
                m = Movie(
                    post_title=self.title,
                    sent_ch=self.ch_sent,
                    sent_en=self.en_sent,
                    pic_url=self.pic,
                    pic_localname="",
                    url=self.url,
                    movie=self.movie
                )
                s.add(m)
                s.commit()
                log_info = "add "+str(self.url)+" to DB successfully..."
                log(log_info)
            else:
                log(str(self.url)+" has already exist...")
            s.close()
        except Exception,e:
            log("error when add to db..."+str(e))

    def handle_charref(self,name):
        try:
            charnum=int(name)
        except ValueError:
            return
        if charnum<1 or charnum>255:
            return
        self.handle_data(chr(charnum))

if __name__ == "__main__":
    pass