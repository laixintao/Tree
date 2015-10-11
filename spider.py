#!/user/bin/env python
#_*_ coding: utf-8 _*_

__author__="laixintao"

import urllib2
import re
from movie import Movie

class Item():
    "data structure"
    sent_ch = ""
    sent_en = ""
    pic = ""
    movie = ""
    url = ""

class LFMspider(object):
    "spider on lessonsfrommocies"
    limit_url = "http://lessonsfrommovies.net/"
    start_url = limit_url
    movies = []

    def start(self):
        html_page = urllib2.urlopen(self.start_url).read()
        self.on_every_page(html_page)

    def on_every_page(self,html):
        num_post = 3 #3 post on each page
        entry_content = re.compile(
            r'entry.content[\s\S]*?\.entry.content')
            # r"<p>[\s\S]*?</p>")
        p = re.compile(r"<p>[\s\S]*?</p>")
        each = entry_content.findall(html)
        for i in each:
            print "---------"
            movie = Movie()
            ps = p.findall(i)
            for ii in ps:
                print ii
        return each

if __name__ == "__main__":
    print "ss"