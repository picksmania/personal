import sys, os
import time
import shutil,subprocess
# Palindrom

'''
f = raw_input("Enter a number/word of your choice... \n")
print type(f)
if f[::1] == f[::-1]:
    print "PALINDROM"
else:
    print "NOT PALINDROM"
'''

# Factorial without recursion/generator
'''
f = raw_input("Enter a number of your choice... \n")
temp =1
if int(f) == 1:
    print "1"
else:
    for i in range(1,int(f)+1):
        temp = temp * i
    print "FACTORIAL iS :::",temp
'''

# Factorial with Generator:
'''
def factorial_gen(number):
    temp=1
    while(number!=1):
        temp=temp*number
        yield temp
        number-=1

p = factorial_gen(5)
print p.next()
print p.next()
print p.next()
print p.next()

'''

# Factorial of number . Linear recursion
'''
def time(n):
    import time
    start = time.time()
    print factorial(n)
    end = time.time()
    exce_time = end - start
    print "time taken", exce_time

def factorial(n):

    sys.setrecursionlimit(1000)
    if n<=1:
        return 1
    else:
        return n*factorial(n-1)

c=time(5)
print c
'''
'''
#files_to_check = [f for f in os.listdir(r'\\datapup.americas.hpqcorp.net\DSCUSER\HPSSA')]
#print files_to_check
networkpath = r'\\datapup.americas.hpqcorp.net'
user = r'ASIAPACIFIC.cpqcorp.net\bagalpr'
password = r'Durga^puja^12345'
#print  os.listdir(r'\\datapup.americas.hpqcorp.net\DSCUSER\Logs')
#winCMD = 'NET USE ' + networkpath + '/user:'+ user + ' '+ password
winCMD = 'NET USE /user:'+ user + ' '+ networkpath + ' ' + password
print "Connecting to the sharepath..."
os.system(winCMD)
#subprocess.Popen(winCMD, stdout=subprocess.PIPE, shell=True)
#shutil.copy2(networkpath + '\DSCUSER\HPSSA',r'\\15.213.141.85\c$\Sharepath\User\Prasit\practice')
'''

import os
'''
file_path = r'C:\pnew_log\test.txt'
with open(file_path,'r') as FH:
    out = FH.read().split()
    #out_lines = FH.read().split()

#n = out.split()

d ={}
print out, type(out)
# print out_lines, type(out_lines)
for i in out:
    if i in d.keys():
        d[i]+=1
    else:
        d[i]=1

print d
print sorted(d.values())
print "*******************************"
final = []
print sorted([(value,key) for (key,value) in d.items()])
# for k,v in d.items():
#     output = k,v
#     final.append(output)
#
# #print sorted(final,key=lambda x:x[1])
# print sorted(final,key=lambda x:len(x[0]))
'''

'''
x = 'ABBABBABBBA'
count = 0
for i in range(0,len(x)):
    if x[i]=='A':
        for j in range(0,i):
            if x[j]=='B':
                count+=1
            else:
                continue

print count

'''
'''
print"====================================================="
print" DECIMAL TO BINARY AND BINARY TO DECIMAL CONVERSION"
print"====================================================="
print" Enter 1 if you want to convert dec to bin"
print" Enter 2 if you want to convert bin to dec"
print"====================================================="
x=input("Enter your choice: ")
if x==1:
  i=1
  s=0
  count =0
  dec=input("Enter decimal to be converted: ")
  while dec>0:
      print "PASS ::",count
      rem=dec%2
      s=s+(i*rem)
      print "S is now:::",s
      dec=dec/2
      i=i*10
      print "i is now....",i
      count+=1

  print "The binary of the given number is ",s,'.'
else:
  bin=raw_input ('Enter binary to be converted: ')
  n=len(bin)
  res=0
  for i in range(1,n+1):
      print int(bin[i-1])
      res=res+ int(bin[i-1])*2**(n-i)
  print "The decimal of the given binary is ",res,'.'
print"====================================================="
'''
'''

x = raw_input("Enter Binary Number::")
print x
print type(x)
s = x[::-1]
sum = 0
print s
for i,x in enumerate(s):
    print i, x
    print "am here"
    if x=='1':
        sum=sum+(2**i)
print sum
'''

# l = [36893488147419103232,36893488147419103232,2,3]
# print id(l)
# print id(l[0])
# print id(l[1])
# print id(l[2])
# print id(l[3])

# LAMBDA
'''
l = [1,2,3,4]
m = [1,2,3,4]
y = map(lambda x:x**2,l)
print y
z = map(lambda x,y:x+y,l,m)
print z
'''

# pass-by-reference-object
# immutable
'''
def func(x):
    print "x is",x
    print "id(x) is",id(x)
    y='def'
    print "y is",y
    print "id(y) is",id(y)

print "id(prasit) is:::",id('prasit')

func('prasit')

x = 'def'
print "X from OUTSIDE:::",x
print id(x)
'''
# mutable
'''
def func(l):
    print "INSIDE FUNCTION...."
    print "l is:",l
    print "id(l) is :", id(l)
    l.append(1)
    print "AFTER APPENDING 1 to l...."
    print "l is:",l
    print "id(l) is :", id(l)
    l.append(2)
    m=l
    print "AFTER APPENDING 1 to l and assigning l to m"
    print "m is:",m
    print "id(m) is :", id(m)


l = [0]
func(l)
print "OUTSIDE l::",l
print "OUTSIDE id(l):",id(l)
'''
'''
with open(r'C:\Prasit\drive_list.txt','r') as FH:
    line = FH.readlines()
print type(line)
print line
print "************************************"
print line[-10:]
print '************************************'
s = [x for x in reversed(line)]
print s
print "************************************"
print line[::-1]
print '+++++++++++++++++++++++++++++++++++++'
if s == line[::-1]:
    print True
'''
#MRO
'''
class A:
    label='a'
    pass
class B(A):
    label='b'
    pass
class C(A):
    label = 'c'
class D(B,C):
    pass
d=D()
print d.label
'''

'''
s = 'i am a boy'
l = s.split()
k = l[::-1]
S = ' '.join(k)
print S
print sys.platform
import platform
print platform.platform()
print platform.python_compiler()
print platform.python_version()
print sys.version
print sys.version_info
'''