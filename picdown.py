__author__ = 'laixintao'

from moviedb import movie_without_pic
import urllib2
from log import log

def download_pictures():
    to_download = movie_without_pic()
    for pic in to_download:
        try:
            print "download ",pic[0]," to ",pic[1]
            imgdata = urllib2.urlopen(pic[1],timeout=50).read()
            file = open(pic[0],"wb+")
            file.write(imgdata)
            file.close()
            log("[O K]download "+pic[0]+" from "+pic[1])
            # print ("[O K]download "+pic[0]+" from "+pic[1])
        except Exception,e:
            log("[ERR]download from "+pic[1]+str(e))
            # print "[ERR]download from "+pic[1]+str(e)

if __name__ == "__main__":
    download_pictures()