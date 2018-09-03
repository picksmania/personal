from threading import *
import os
import re
import time
import datetime
import sys


class ipaddress():
    def __init__(self):
        self.time = 0

    def ipadd(self):
        pat = re.compile(r"(\d) received")
        report = ('No response','Partial response','Alive')

        stime = datetime.datetime.now()

        for host in range(60,70):
            ip = '10.41.29.'+str(host)
            channel = os.popen("ping -q -c2 "+ip, 'r')
            print "Testing....",ip
            while True:
                line=channel.readline()
                if not line:break
                result = re.findall(pat,line)
                if result:
                    print report[int(result[0])]

        etime = datetime.datetime.now()

        total_time = etime - stime
        return total_time

    def getTime(self):
        final_time = self.ipadd()
        return final_time

class Player(Thread):
    def __init__(self,lock,itemq,sleeptime=1):
        Thread.__init__(self)
        self.itemq = itemq
        self.lock = lock

    def run(self):
        lock = self.lock
        itemq = self.itemq
        i= 0
        while i<3:
            lock.acquire()
            #cur = itemq.getValue()
            #print "Current Value is:::",cur+1
            itemq.ipadd()
            #itemq.adder()
            lock.release()
            i = i+1




q = ipaddress()
lock = Lock()

p1 =Player(lock,q)
p2 =Player(lock,q)
p3 =Player(lock,q)

p1.start()
p2.start()
p3.start()


p1.join()
p2.join()
p3.join()

print "FINAL VALUE====",q.getTime()