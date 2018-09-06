# Exercise 3:
'''
list = [1,1,2,3,4,5,8,7,65,32,45,9]
print [x for x in list if x<10]
print filter((lambda x: x<5),list)
print map((lambda x: x<5),list)
'''

'''
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

print [x for x in a if x in b]
print [x for x in a if x%2==0]
print [(x,y) for x in a for y in b if x == y]
'''


# Question:
# Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence

'''
import math
c=50
h=30
value = []
items=[x for x in raw_input().split(',')]
for d in items:
    value.append(str(int(round(math.sqrt(2*c*float(d)/h)))))

print ','.join(value)

'''

# Question:
# Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array.
# The element value in the i-th row and j-th column of the array should be i*j.

# Example
# Suppose the following inputs are given to the program:
# 3,5
# Then, the output of the program should be:
# [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]
'''
input_str = raw_input("please enter two digits...\n")
dimensions=[int(x) for x in input_str.split(',')]
rowNum=dimensions[0]
colNum=dimensions[1]
multilist = [[0 for col in range(colNum)] for row in range(rowNum)]
print multilist

for row in range(rowNum):
    for col in range(colNum):
        multilist[row][col]= row*col
print multilist
'''

'''
s =raw_input("enter a string:: \n")
#print s, type(s)
l = []
m = []
l.append(s.upper())
for sentence in l:
    print sentence
print l
new_list = [x for x in s.split(' ')]
print ' '.join(sorted(set(new_list)))
'''

# Question:
# Write a program which accepts a sequence of comma separated 4 digit binary numbers as its input
# and then check whether they are divisible by 5 or not. The numbers that are divisible by 5 are to be printed in a comma separated sequence.
# Example:
# 0100,0011,1010,1001
# Then the output should be:
# 1010

'''
value = []
items=[x for x in raw_input().split(',')]
for p in items:
    intp = int(p, 2)
    print intp
    if not intp%5:
        value.append(p)

print ','.join(value)
'''

# Question:
# Write a program that accepts a sentence and calculate the number of upper case letters and lower case letters.
# Suppose the following input is supplied to the program:
# Hello world!
# Then, the output should be:
# UPPER CASE 1
# LOWER CASE 9
'''
s = raw_input("Print a sentence with DIGIT and Alphabet::::: \n:::")
d = {'DIGIT':0,'LETTER':0}
print type(d)
for i in s:
    print i
    if i.isdigit():
        d['DIGIT']+=1
    elif i.isalpha():
        d['LETTER'] +=1
    else:
        pass
print "LETTERS", d['LETTER']
print "DIGITS", d['DIGIT']
'''
'''
list = [1,2,3,20,22,50,5,6,7,9,8,9,10]
new_list =[]
#print len(list)
for i in range(0,len(list)-1):
     print list[i], list[i+1]
     if list[i]+1 == list[i+1]:
        if (list[i] and list[i+1]) not in new_list:
            new_list.append(list[i])
            new_list.append(list[i+1])

print set(new_list)
'''
# Find all possible combination of characters in a string using recursion
'''
import itertools
str = 'prasit'
k=3
permutations = ["".join(x) for x in itertools.permutations(str,k)]
print permutations
print "***********************************************************"
for p in itertools.product(str, repeat=3):
    print p
'''

# count number of charcter in a string
'''
str = 'aabbbdddcccddeefff'
dict = {}
for n in str:
    keys = dict.keys()
    values = dict.values()
    print keys,values
    if n in keys:
        dict[n] += 1
    else:
        dict[n] = 1
print dict
'''
#
# Write a Python program to get a string made of the first 2 and the last 2 chars from a given a string.
# If the string length is less than 2, return instead of the empty string
'''
s = 'Prasita'
s_len = len(s)
print s_len
if s_len < 2:
    print s
else:
    first_two = s[:2]
    last_two = s[-2:]
    print first_two,last_two
    new_str = first_two + last_two
    print new_str
'''
#
# Write a Python program to get a string from a given string where all occurrences of its
# first char have been changed to '$', except the first char itself.
'''
s = 'restart'
first_char = s[0]
s = s.replace(first_char,'$')
s1 = first_char + s[1:]
print s1
'''

# Write a Python program to get a single string from two given strings, separated by a space
# and swap the first two characters of each string
'''
s = 'xyz','abc'
print len(s)
a = s[0][:2]
print "a:",a
b = s[1][:2]
print "b:",b
print b+s[0][2:]+a+s[1][2:]
'''

# Write a Python program to add 'ing' at the end of a given string (length should be at least 3).
# If the given string already ends with 'ing' then add 'ly' instead.
# If the string length of the given string is less than 3, leave it unchange
'''
s = 'abcdefing'

if len(s)> 3:
    last_three = s[-3:]
    print last_three
    s1 = s.replace(last_three,'ing')
    print s1
    if last_three == 'ing':
        s1 = s.replace(last_three,'ly')
        print s1
'''


# Write a Python program to count and display the vowels of a given text.
'''
V = 'aeiou'
s = 'Prasit Bagal Rinki Dey Sunanda'
d = {}
for i in s:
    keys = d.keys()
    if i in V:
        if i in keys:
            d[i]+= 1
        else:
            d[i] = 1
print d
'''

# Write a Python program to split a string on the last occurrence of the delimiter.
'''
str1 = 'abc,def,ghi,jkl,mnop'
print(str1.rsplit(',', 1))
print(str1.rsplit(',', 2))
print(str1.rsplit(',', 5))
print "*****************************"
print(str1.split(',', 1))
'''

# Swap comma and dot in a string
# print character with positions
'''
from string import maketrans

s = '32.888,abcd!Prasit'
trantab = maketrans('.,!',',.+')
print s.translate(trantab)
for i,x in enumerate(s):
    print i,x
'''

# Write a Python program to strip a set of characters from a string
'''
str = 'The quick brown fox jumps over the lazy dog.'
chars = 'aeiou'
new_str = ''.join(x for x in str if x not in chars)
print new_str
'''

# Write a Python program to reverse a string
'''
str = 'The quick brown fox jumps over the lazy dog'
str1 = 'prasitbagal'
print "1::",str1[::-1]
print "2::",str1[:-1]
print "3::",str1[::2]
print "4::",str1[4::-1]
print "5::",str1[4:-1]
print "6::",str1[-1::-2]
for i,x in enumerate(str1):
    print i,x

'''
# Write a Python program to count occurrences of a substring in a string.
'''
str = 'The quick brown fox jumps over the lazy dog. Dog jums over the cat. Cat loves fish. fox fox fox !!!!'
sub = 'fox'

print str.lower().count('dog')
print str.find('fox')
'''


# Write a Python program to display a number in left, right and center aligned of width 10.
'''
x =20000000
print("Left aligned (width 10)   :"+"{:< 10d}".format(x))
print("Right aligned (width 10)  :{:10d}".format(x))
print("Center aligned (width 10) :"+"{:^10d}".format(x))
print("Formatted number with comma separated :"+"{:,}".format(x))
'''

# Write a Python function that takes a list of words and returns the length of the longest one.
'''
world_lrn = []
list = ['prasit','Automation','Driver Smart','bagal']
for i in list:
    world_lrn.append((len(i),i))
print world_lrn
world_lrn.sort()
print world_lrn
print world_lrn[-1][1]
'''

'''
number = []
for i in range(1000):
    num = str(i).zfill(3)
print num
number.append(num)

import random
t = random._sqrt(r)
'''

# *************************** END OF STRING TEST EXERCISES **********************************

# Write a Python program to add two positive integers without using the '+' operator.
'''
def bitwise_add(a,b):
    # a = 22    #
    # b = 10
    i =1#
    while b!=0:
        print "***** PASS NUMBER ******",i
        c = a&b   # carry
        print "a AND b",c
        a = a^b   # addition
        print "a XOR b",a
        print "LEFT SHIFT c by 1 and store the result in b"
        b = c <<1  # leftshift
        print "new b::",b
        i+=1
    print a
    return a

bitwise_add(4,10)

def bitwise_sub(a,b):
    return bitwise_add(a,bitwise_add(~b,1))

#bitwise_sub(22,10)
'''



# Write a Python program to get all possible two digit letter combinations from a digit (1 to 9) string.
# string_maps = {
# "1": "abc",
# "2": "def",
# "3": "ghi",
# "4": "jkl",
# "5": "mno",
# "6": "pqrs",
# "7": "tuv",
# "8": "wxy",
# "9": "z"
# }
'''

def digit_combination(a):
    d = {
    "1": "abc",
    "2": "def",
    "3": "ghi",
    "4": "jkl",
    "5": "mno",
    "6": "pqrs",
    "7": "tuv",
    "8": "wxy",
    "9": "z"
    }
    if a == '':
        print "NO NUMBERS...."
        return None
    else:
        key1 = a[0]
        key2 = a[1]
        if (key1 and key2) in d.keys():
            print "both KEYS are available"
            key1_val = d.get(key1)
            key2_val = d.get(key2)
            NEW_LIST = []
            for i in key1_val:
                for j in key2_val:
                    NEW_LIST.append(i+j)
            print NEW_LIST
            return NEW_LIST

        else:
            print "KEYS are not available"


digit_combination('20')
'''


# Write a Python program to create all possible permutations from a given collection of distinct numbers
'''
import itertools
def permutation(a):
    if a == '':
        print "NO VALUE..."
    else:
        new_list = list(map("".join, itertools.permutations(a)))
        # new_list = list(itertools.permutations(a))
        # new_list = itertools.permutations(a)
        # for i in new_list:
        #     print i
        print new_list
permutation('BAC')

'''
'''
def all_perms(elements):
    new_list = []
    if len(elements) <=1:
        yield elements
    else:
        for perm in all_perms(elements[1:]):
            for i in range(len(elements)):
                print perm[:i] + elements[0:1] + perm[i:]
                # nb elements[0:1] works in both string and list contexts
                yield perm[:i] + elements[0:1] + perm[i:]
                #new_list.append(perm[:i] + elements[0:1] + perm[i:])


x = all_perms('abc')
for i in x:
    print i
'''

# Write a Python program to display some information about the OS where the script is running
'''
import os
import platform as pl

print pl._abspath
print pl._default_architecture
print pl._sys_version()
print pl.dist()
print pl.mac_ver()
print pl.machine()
print pl.platform()
'''

# Write a Python program to get a list of locally installed Python modules
'''
import pip

installed_packages = pip.get_installed_distributions()
installed_packages_list = sorted(["%s==%s" % (i.key, i.version) for i in installed_packages])
print(installed_packages_list)
'''

# Write a Python program to count the number of each character of a given text of a text file.
'''
str = 'aaabbbccdddaaa44555'
with open(r'C:\pnew_log\new_log\summarylog_2017-07-13-04-22-12.txt','r') as f:
    str1 = f.readlines()
    # print type(str1)
    print str1
    str2 = '|'.join(str1)
    print str2
    print type(str2)
    d ={}
    for i in str2:
        keys = d.keys()
        values = d.values()
        if i in keys:
            d[i]+=1
        else:
            d[i]=1

    print d
'''
'''
import collections
with open(r'C:\pnew_log\new_log\summarylog_2017-07-13-04-22-12.txt','r') as f:
  count = collections.Counter(f.read().upper())
  print count

'''

# Write a Python program to print a long text, convert the string to a list and print all the words and their frequencies
'''
with open(r'C:\pnew_log\test.txt','r') as f:
  str = f.read()
  print str, type(str)

words_list = str.split(' ')
#print words_list, type(words_list)
new_count_list = []

for i in words_list:
  new_count_list.append((i,len(i)))
print new_count_list
'''

# Write a Python program to create all possible strings by using 'a', 'e', 'i', 'o', 'u'. Use the characters exactly once
'''
import itertools
str = 'aeiou'
perm = itertools.permutations(str)
for i in perm:
  print i,type(i)
'''

# Write a Python program to remove and print every third number from a list of numbers until the list becomes empty
'''
A_list = [1,5,10,15,20,25,30,35,40,45,50]
#s = A_list.__delitem__(3)

while len(A_list)>2:
   #A_list.__delitem__(3)
   item = A_list.__getitem__(2)
   print item
   delete_item = A_list.__delitem__(2)
   print A_list

# A_list.__setitem__(11,100)
# print A_list
'''

# Write a Python program to get the top stories from Google news.
'''

import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url="https://news.google.com/news/rss"
Client=urlopen(news_url)
xml_page=Client.read()
Client.close()

soup_page=soup(xml_page,"xml")
news_list=soup_page.findAll("item")
# Print news title, url and publish date
for news in news_list:
  print(news.title.text)
  print(news.link.text)
  print(news.pubDate.text)
  print("-"*60)

'''

'''
str = 'prasit bagal'
str1 = 'abba'

print "String is::::",str
print "str[1:4]***",str [1:4]
print "str[-4:]***",str[-4:]
print "str[:-1]***",str[:-1]
print "str[::-1]***",str[::-1]
print "str[::]",str[::]
print "str[::-2]",str[::-2]
print "str[:4:-1]",str[:4:-1]
print "str[-6:-1:-2]",str[-6:-1:-2]

print "******check**********"
if str1[:] == str1[::-1]:
    print 'PALINDROM'
'''

# Swap every two bits in bytes
# Before swapping: 11-10-11-01
# After swapping: 11-01-11-10
'''
import math
one_byte = 4
# if len(one_byte)!= 8:
#     print 'Need exact one Byte...'


x = ((one_byte & 0b10101010) >> 1) or ((one_byte & 0b01010101) << 1)
print x
'''


# SORT a list without using any builtin function
'''
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
new_list = []
# 1st approach:::

while data_list:
    minimum = data_list[0]  # arbitrary number in list
    for x in data_list:
        if x < minimum:
            minimum = x
    new_list.append(minimum)
    data_list.remove(minimum)

print new_list

# 2nd approach:::
# for i in range(len(data_list)):
#     a = min(data_list)
#     new_list.append(a)
#     data_list.remove(a)
#
# print new_list
'''
# drive_id = ['1E:2:2', '1E:2:9', '1E:2:10', '1E:1:16', '1E:1:14', '1E:1:7', '1E:1:18', '1E:2:24', '1E:2:12', '1E:1:15', '1E:2:1', '1E:1:2', '1E:1:17', '1E:1:12', '1E:1:1', '1E:1:8', '1E:2:7', '1E:1:9', '1E:1:19', '1E:1:10', '1E:1:24', '1E:1:23', '1E:2:13', '1E:1:11']
# d = {'MO0400JFFCF_MO0800JFFCH_MO1600JFFCK_MO3200JFFCL': ['MO0800JFFCH'], 'MM1000GFJTE': ['MM1000GFJTE'], 'VK0240GEPQN_VK0480GEPQP_VK0960GEPQQ': ['VK0240GEPQN'], 'EG0300JFCKA_EG0600JEMCV_EG0900JFCKB_EG1200JEMDA': ['EG1200JEMDA'], 'VK0120GFDKE_VK0240GFDKF_VK0480GFDKH_VK0960GFDKK_VK1920GFDKL_VK3840GFDKN': ['VK0960GFDKK'], 'VO0480JFDGT_VO0960JFDGU_VO1920JFDGV_VO3840JFDHA': ['VO0480JFDGT', 'VO0960JFDGU'], 'MO0200JEFNV_MO0400JEFPA_MO0800JEFPB_MO1600JEFPC_EO0200JEFPD_EO0400JEFPE_EO0800JEFPF': ['MO0200JEFNV', 'EO0200JEFPD'], 'EG001800JWFVC': ['EG001800JWFVC', 'EG001800JWFVC'], 'EG1800JEMDB': ['EG1800JEMDB'], 'EG0300FCSPH_EG0450FCSPK_EG0600FCSPL_EG0900FCSPN': ['EG0600FCSPL'], 'EH000300JWCPK_EH000600JWCPL_EH000900JWCPN': ['EH000300JWCPK', 'EH000600JWCPL', 'EH000900JWCPN'], 'EH0300JDYTH_EH0450JDYTK_EH0600JDYTL': ['EH0450JDYTK'], 'EH0300JDXBA_EH0450JDXBB_EH0600JDXBC': ['EH0300JDXBA'], 'EH0300JEDHC_EH0450JEDHD_EH0600JEDHE': ['EH0450JEDHD'], 'EG0300JEHLV_EG0600JEHMA_EG0900JEHMB_EG1200JEHMC': ['EG0900JEHMB', 'EG1200JEHMC'], 'VO1920JEUQQ': ['VO1920JEUQQ'], 'EG0600JETKA_EG0900JETKB_EG1200JETKC': ['EG0600JETKA'], 'MK0960GECQK': ['MK0960GECQK'], 'EG000300JWBHR': ['EG000300JWBHR', 'EG000300JWBHR']}
# if d.has_key('MK000240GWKVK_MK000480GWJPN_MK000960GWJPP'):
#     print "KEY PRESENT"

# d_id = {'MB6000GEBTP': '1E:1:11', 'MB3000GCVBT': '1E:2:7', 'MB6000JVYYV': '1E:1:4', 'MB4000JVYZQ': '1E:1:6', 'MB6000GVYYU': '1E:2:8', 'MB6000GEXXV': '1E:2:4', 'MB8000JFECQ': '1E:2:10'}
# d_model = {'MB6000GEBTP': ['MB6000GEBTP'], 'MB1000JVYZL_MB2000JVYZN_MB3000JVYZP_MB4000JVYZQ': ['MB4000JVYZQ'], 'MB6000JVYYV': ['MB6000JVYYV'], 'MB6000GVYYU': ['MB6000GVYYU'], 'MB6000GEXXV': ['MB6000GEXXV'], 'MB8000JFECQ': ['MB8000JFECQ', 'MB8000JFECQ'], 'MB2000GCVBR_MB3000GCVBT_MB4000GCVBU': ['MB3000GCVBT']}
'''
import re
with open(r'C:\Prasit\SNAP3_all_drive.txt','r') as f:
    #data = f.read().splitlines()
    data = f.read().splitlines()
    for i in data:
        #print i
        s = re.sub('\s+', '_', i)

        print s
print "************************************************"
#print data
'''

