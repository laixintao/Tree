import urllib2
import time
from MovieHtmlParser import MovieHtmlParser

class LFMspider(object):
    "spider on lessonsfrommocies"
    limit_url = "http://lessonsfrommovies.net/"
    start_url = limit_url

    def start(self):
        begin = MovieHtmlParser()
        timeout_url = []
        npl = "http://lessonsfrommovies.net/?paged="
        for i in range(85,611):
            url = npl+str(i)
            print url,
            try:
                html = urllib2.urlopen(url,
                                       timeout=10).read()
            except Exception,e:
                timeout_url.append(url)
                print "timeout"
                continue
            html = begin.unescape(html)
            begin.feed(html)
            print "ok"
            time.sleep(10)
        begin.close()
        for u in url:
            print u
        file = open("timeout_url.txt","w")
        for u in timeout_url:
            file.write(u)
        file.close()

