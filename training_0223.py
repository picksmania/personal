
# Generator:
'''
def sequence(x):
    a=2
    if x==0:i=0
    if x==1: i=1
    while True:
        i = i+a
        yield i

evenseq = sequence(0)
oddseq = sequence(1)

for i in range(10):
    print next(evenseq)


'''
# PRIME GENERATORS

# def prime(n):
#     for x in range(1,n):
#         prime = True
#         for i in range(2,x):
#             if (x%i==0):
#                 prime = False
#         if prime == True:
#            yield x
#
# gen = prime(100)
# print type(gen)
# for i in gen:
#     print i
'''
def testprime(m):
    if m<2: return False
    i=2
    while i<m:
        if m % i == 0:
            return False
        i = i+1
    return True
'''
#======================================================
import os
import re
import time
import sys



received_packages = re.compile(r"(\d) received")
status = ("no response","alive but losses","alive")

for suffix in range(50,60):
   ip = "10.41.105."+str(suffix)
   ping_out = os.popen("ping -q -c2 "+ip,"r")
   print "... pinging ",ip
   while True:
       line = ping_out.readline()
       if not line: break
       n_received = received_packages.findall(line)
       if n_received:
           print ip + ": " + status[int(n_received[0])]

print n_received


































