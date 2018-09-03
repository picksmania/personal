from threading import *
import time
import threading
from multiprocessing.dummy import Pool as ThreadPool
import multiprocessing as mp
import datetime
import os
import re
import time
import sys
'''
class itemQ():
    def __init__(self):
        self.count = 0

    def adder(self):
        self.count+=1

    def getValue(self):
        return self.count

class Player(Thread):
    def __init__(self,lock,itemq,sleeptime=1):
        Thread.__init__(self)
        self.itemq = itemq
        self.lock = lock

    def run(self):
        lock = self.lock
        itemq = self.itemq
        i,cur = 0,0
        while i<1000:
            lock.acquire()
            cur = itemq.getValue()
            print "Current Value is:::",cur+1
            itemq.adder()
            lock.release()
            i = i+1

q = itemQ()
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

print "FINAL VALUE====",q.getValue()
'''

'''
def sleeper(i):
    print "thread %d sleeps for 5 seconds" % i
    time.sleep(5)
    print "thread %d woke up" % i

for i in range(10):
    t = Thread(target=sleeper, args=(i,))
    t.start()
'''
'''
class PrimeNumber(threading.Thread):
  def __init__(self, number):
    threading.Thread.__init__(self)
    self.Number = number

  def run(self):
    counter = 2
    while counter*counter < self.Number:
      if self.Number % counter == 0:
        print "%d is no prime number, because %d = %d * %d" % ( self.Number, self.Number, counter, self.Number / counter)
        return

      else:
        print "%d is a prime number" % self.Number
      counter += 1
threads = []
while True:
    input = long(raw_input("number: "))
    if input < 1:
        break

    thread = PrimeNumber(input)
    threads += [thread]
    thread.start()

for x in threads:
    x.join()
'''
'''
class PrimeNumber(threading.Thread):
    prime_numbers = {}
    lock = threading.Lock()

    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[number] = "None"
        PrimeNumber.lock.release()

    def run(self):
        counter = 2
        res = True
        while counter*counter < self.Number and res:
            if self.Number % counter == 0:
               res = False
            counter += 1
        PrimeNumber.lock.acquire()
        PrimeNumber.prime_numbers[self.Number] = res
        PrimeNumber.lock.release()
threads = []
while True:
    input = long(raw_input("number: "))
    if input < 1:
        break

    thread = PrimeNumber(input)
    threads += [thread]
    thread.start()
print threads
for x in threads:
    x.join()
'''

#=================================================

import urllib2
from multiprocessing.dummy import Pool as ThreadPool
import datetime

stime =datetime.datetime.now()

urls = [
  'http://www.python.org',
  'http://www.python.org/about/',
  'http://www.onlamp.com/pub/a/python/2003/04/17/metaclasses.html',
  'http://www.python.org/doc/',
  'http://www.python.org/download/',
  'http://www.python.org/getit/',
  'http://www.python.org/community/',
  'https://wiki.python.org/moin/',
  ]

# make the Pool of workers
#pool = ThreadPool(1)

# open the urls in their own threads
# and return the results
#results = pool.map(urllib2.urlopen, urls)
#print results
# close the pool and wait for the work to finish
#pool.close()
#pool.join()
#etime = datetime.datetime.now()
#finish_time=etime-stime
#print "TIME TAKEN:::",finish_time



stime =datetime.datetime.now()
# PING IP address in a range
'''
pat = re.compile(r"(\d) received")
report = ('No response','Partial response','Alive')


def ip_check(x):
    ip = '10.41.105.'+str(x)
    channel = os.popen("ping -q -c2 "+ip, 'r')
    print "Testing....",ip
    time.sleep(1)
    while True:
        line=channel.readline()
        if not line:break
        result = re.findall(pat,line)
        if result:
            print report[int(result[0])]
        return result
'''

def prime_number(m,n):
    print "Start Number is  %s and End Number is %s"%(m,n)
    for x in range(m,n):
        prime = True
        for i in range(2,x):
            if (x%i==0):
                prime = False
        if prime == True:
            print x
    print('module name:', __name__)
    print('parent process:', os.getpid())
    print('process id:', os.getpid())


'''
def cube(x):
    return x**3
'''


#============ GATHER_python_file ===================
'''
def python_file_check():
    curr_dir = os.getcwd()
    listdir = os.listdir(curr_dir)
    d ={}
    #cache_file_name =collections.defaultdict(dict)
    cache_file_name={}
    all_file =[]
    for i in listdir:
        if i.endswith('py'):
            cache_file_name[i]={}
    print "ALL FILE in DICT::",cache_file_name

    for k,v in cache_file_name.items():
        file_path = os.path.join(curr_dir,k)
        all_file.append(file_path)
    print "ALL file in LIST::",all_file

    for i in all_file:
        file_name = i
        print file_name,type(file_name)
        pat = r'[^\\]*py$'
        python_file_name = re.findall(pat,i)
        #print python_file_name,type(python_file_name)

        indi_file_name = python_file_name[0]
        FR = open(i,'r')
        read_file = FR.read()
        read_lines = read_file.split('\n')

        if_count =0
        for_count =0
        for i in read_lines:
            if i.__contains__('if'):
                if_count+=1
            if i.__contains__('for'):
                for_count+=1

        print "NUmber of IF Loop is:",if_count
        print "Number of FOR loop is",for_count

        print "**************************************************"

        if cache_file_name.has_key(indi_file_name):
            cache_file_name[indi_file_name]['if']=if_count
            cache_file_name[indi_file_name]['for']=for_count

    #print cache_file_name
    return cache_file_name
'''''


#pool = ThreadPool(4)
# pool1 = mp.Pool(processes=1)
# #results = pool.map(python_file_check)
# results = pool1.apply(prime_number,args=(10,10000))
# #print results
# # close the pool and wait for the work to finish
# pool1.close()
# pool1.join()

# def info(title):
#     print(title)
#     print('module name:', __name__)
#     print('parent process:', os.getppid())
#     print('process id:', os.getpid())

# def f(name):
#     info('function f')
#     print('hello', name)

# etime = datetime.datetime.now()
# finish_time=etime-stime
# print "TIME TAKEN:::",finish_time


if __name__ == '__main__':
    pool1 = mp.Pool(processes=1)
    #pool = ThreadPool(5)
    #results = pool1.apply(prime_number,args=(10,5000))
    #results = [pool1.apply(cube,args=(x,)) for x in range(1,10000)]
    results = [pool1.apply(ip_check,args=(x,)) for x in range(50,100)]
    #results = pool.map(ip_check,[x for x in range(50,100)])
    #results = [pool1.apply(cube,args=(x,)) for x in range(1,100)]
    #results = [pool1.apply(python_file_check)]
    #results1 = pool.map(cube,[x for x in range(1,10000)])
    #results1 = pool.map(python_file_check)
    print results
    #print results1
    # close the pool and wait for the work to finish
    pool1.close()
    pool1.join()
    etime = datetime.datetime.now()
    finish_time=etime-stime
    print "TIME TAKEN:::",finish_time

    # import platform
    # print('\nPython version  :', platform.python_version())
    # print('compiler        :', platform.python_compiler())
    #
    # print('\nsystem     :', platform.system())
    # print('release    :', platform.release())
    # print('machine    :', platform.machine())
    # print('processor  :', platform.processor())
    # #print('CPU count  :', platform.cpu_count())
    # print('interpreter:', platform.architecture()[0])