# def validateipaddress(*ip):
#     valid_ip = []
#     invalid_ip =[]
#     ip_list = ip
#     print ip_list
#     for i in ip_list:
#         L = i.split('.')
#         if len(L) != 4:
#             invalid_ip.append(i)
#         flag = True
#         for x in L:
#             if not x.isdigit():
#                 invalid_ip.append(i)
#                 flag=False
#             else:
#                 x = int(x)
#                 if x<1 or x>255:
#                     invalid_ip.append(i)
#                     flag=False
#         if flag==True:
#             valid_ip.append(i)
#
#     print "VALID IP::", valid_ip
#     print "INVALID IP::",invalid_ip
#     return valid_ip,invalid_ip
#
#
# validateipaddress('15.23.21.89','16.222.34.566','10.10.10.124')
##########################################################################################

# a = [1,2,3,4,5]
# b = [11,22,33,44,55]
# c = [[1,2,3],[4,5,6],[7,8,9]]
# d = [[10,20,30],[40,50,60],[70,80,90]]
# print zip(a,b)
# print zip(*c)
# x = zip(*c)
# y = zip(*d)
#
# for i in x:
#     print sum(i)
#################################################################################
'''
import sys
if len(sys.argv) != 3:
    print 'I need 2 input the CLI'
    sys.exit(1)

x = int(sys.argv[1])
y = int(sys.argv[2])
z = x+y
print 'SUM is',z
'''
#################################################################################
# Write a script to copy the content of first N-1 files into Nth File using cli
# Here we need to copy 4 files content to last file
'''
import sys
if len(sys.argv) <3:
    print 'I need minimum 2 input file names...'
    sys.exit(1)
list_of_files = []
for i in range(1,len(sys.argv)):
    list_of_files.append(sys.argv[i])

write_file_name = list_of_files[-1]
fout = open(write_file_name,'a+')
for item in list_of_files:
    with open(item,'r') as f1:
        lines = f1.readlines()
        fout.writelines(lines)

'''
####################################################################################
# write a script to split file into N parts
# python filesplit.py temp.dat 4 --> here it will split the file based on the BYTE. if temp.dat is 100 byte then it should divide 25 byte to each file.
# if its 101 BYTE then first 3 will have 25 bytes and last will have 26 byte

'''
import sys
if len(sys.argv) <2:
    print 'I need minimum 1 input file names...'
    sys.exit(1)

input_file = sys.argv[1]
fh = open(input_file,'r')
fh.seek(0,2)
size_of_file = fh.tell()
fh.seek(0,0)
each_file_size = size_of_file/4
print each_file_size
fh = open(input_file,'r')

for i in range(1,5):

    data = fh.read(each_file_size)
    fout = open(r'C:\Prasit\temp_%s.txt'%i,'w')
    fout.write(data)

fout.close()
'''

##############################################################################################################
'''
import sys
if len(sys.argv) <2:
    print 'I need minimum 1 input file names...'
    sys.exit(1)

input_file = sys.argv[1]
FR = open(input_file,'r')
# fh.seek(0,2)
# s = fh.read()
# print s
for x in xrange(10):
    line = next(FR)
    print line

'''
##############################################

import re
# write a script to find SUM of all the numbers available in a string
'''
str = 'abcd efg 100 rm$:- 400 350 100 defg'
pat = '\d+'
all_number = re.findall(pat,str)
sum =0
for i in all_number:
    sum=sum+int(i)

print sum
'''

###############################################
# write a script to extract all words which contains at least one Vowel in a string
'''
str = 'Man dog 100 $:- 400 Sky 350 cat KKK RainBow dad bad pen Goat Watch KKR BLR Ccu IxB'
pat = '\w?[AEIOUaeiou]\w+'
all_words = re.findall(pat,str)
print all_words
'''
###############################################

# write a script to extract all the words which begins with Capital letter from a string
'''
str = 'Man dog 100 $:- 400 Sky 350 cat KKK RainBow dad bad pen Goat Watch KKR BLR Ccu IxB'
pat = '[A-Z]\w+'
caps_word = re.findall(pat,str)
print caps_word
'''

##########################################################

# write a script to extract all the words which begins with Capital letter and ends with small letter vowel
'''
str = 'Man dog 100 $:- 400 Sky 350 cat KKK RainBow dad bad pen Goat Watch KKR BLR Ccu IxB'
pat = '[A-Z]\w+[a-z]'
caps_word = re.findall(pat,str)
print caps_word
'''

#########################################################
# write  a script to extract all CAPITAL letter word from a string
'''
str = 'Man dog 100 $:- 400 Sky 350 cat KKK RainBow dad bad pen Goat Watch KKR BLR Ccu IxB xyz'

pat = r'\b[A-Z]+\b'
caps_word = re.findall(pat,str)
print caps_word
'''

#to extract all valid IP address in a string.
'''
s = raw_input("Enter an IP...")

pat = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
if re.match(pat,s):
    print "VALID IP"
else:
    print "INVALID IP"
'''
#####################################################
# write  a script to extract all the numbers between 1 and 255 inclusive




