import re

'''
with open(r'C:\pnew_log\prasit_final_summary_log_0203.txt', 'r') as f:
    print f
    print f.seek(0)
    print "TELL()::",f.tell()
    all_str = f.readlines()[-10:]
    print all_str
    str= ','.join(all_str)
    print str
    #print type(f.read())
    #print f.tell()
    pat = '\d{2,4}\.\d{2,4}\.\d{2,4}\.\d{2,4}'
    pat1 = 'HP\w\d'
    m = re.findall(pat,str)
    n = re.findall(pat1,str)
    print m
    print n
    # print "======= Counting Space and Tab pf given File =============="
    # space =0
    # tab = 0
    # i =0
    # for i,x in enumerate(f):
    #     #print "LINE NUmber {0:2d} FIle {1:2d}".format(i,x)
    #     #print i,x
    #     space += x.count(' ')
    #     tab += x.count('\t')
    #     print "Line {0:2d} Sapce {1:2d} Tab {2:2d}".format(i,space,tab)
    # print "==================================="
    # print f.readline()
    # print "==================================="
    # print f.seek(-1024,2)
    # print f.tell()
    # print "==================================="
    # print f.readlines()
    # print type(f.readlines())
'''

# READ a file of big size

import faker
