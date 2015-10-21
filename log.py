from config import DETAIL_LOG_PATH
from config import TIME_OUT_LOG_PATH
from time import strftime
import time

class Log(object):
    "must be run del method!"
    def __init__(self):
        self.log_file = open(DETAIL_LOG_PATH,"a")
        self.timeout_log_file = open(TIME_OUT_LOG_PATH,"a")

    def local_time(self):
        "[20151021-Wed 22:27:17]"
        return strftime("[%Y%m%d-%a %H:%M:%S]")

    def log(self,msg):
        if type(msg) == type("str"):
            self.log_file.write(
                self.local_time()+msg)
            self.log_file.write("\n")
        else :
            #todo
            pass


    def log_timeout(self,url):
        self.timeout_log_file.write(url+"\n")

    def __del__(self):
        self.log_file.close()
        self.timeout_log_file.close()
        # to test if the __del__ is actually called
        # print "del..."

lf = Log()

# public function
def log(msg):
    lf.log(msg)

def logtimeout(url):
    lf.log_timeout(url)


if __name__ == "__main__":
    print "test local_time()..."
    print Log().local_time()
    print "test log()..."
    log("test log...")
    for i in range(10):
        print "test log..."+str(i)
        log("test log..."+str(i))
        time.sleep(1)
    logtimeout("123")
    print "test ok."