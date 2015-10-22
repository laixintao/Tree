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

    def parser_pages(self,start_page,end_page,timeleg=10):
        for i in range(start_page,end_page+1): # include the end_page
            time.sleep(timeleg)
            self.parser_one_page(i)

    def parser_all_pages(self,timeleg=10):
        self.parser_pages(1,600,timeleg)

if __name__ == "__main__":
    lfs = LFMSpider()
    print "parser page..."
    lfs.parser_one_page(14)
    lfs.parser_one_page(15)
    lfs.parser_one_page(16)
    # for i in range(43,46):
    #     lfs.parser_one_page(i)
    # print "finish"
    # print "test parser pages...2 to 20"
    # lfs.parser_pages(2,20)

