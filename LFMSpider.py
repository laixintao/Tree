import urllib2
import time
from MovieHtmlParser import MovieHtmlParser
from config import START_PAGE,END_PAGE
from log import log,logtimeout
class LFMSpider(object):
    "spider on lessonsfrommocies"
    limit_url = "http://lessonsfrommovies.net/"
    next_page_url_head = "http://lessonsfrommovies.net/?paged="

    def parser_one_page(self,page_num):
        mhp = MovieHtmlParser()
        url = self.next_page_url_head + str(page_num)
        print url,
        log("start parser page"+str(page_num))
        try:
            html = urllib2.urlopen(url,
                                   timeout=10).read()
            log("open..."+url+"...ok")
        except Exception,e:
            log("error in open url"+"..."+str(e))
            print "timeout"
            logtimeout(url)
        try:
            html = mhp.unescape(html)
            mhp.feed(html)
            print "ok"
            log("html parser..."+"ok")
        except Exception,e:
            log("error..."+str(e))
        finally:
            mhp.close()

if __name__ == "__main__":
    lfs = LFMSpider()
    print "parser page..."
    lfs.parser_one_page(12)
    for i in range(43,46):
        lfs.parser_one_page(i)
    print "finish"

