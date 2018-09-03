import re
import os
import collections

curr_dir = os.getcwd()
listdir = os.listdir(curr_dir)
d ={}
#cache_file_name =collections.defaultdict(dict)
cache_file_name={}

for i in listdir:
    if i.endswith(('py','pyc')):
        cache_file_name[i]={}

user_file_name = raw_input("Enter the file name::")
if cache_file_name.has_key(user_file_name):
    print "YOUR FILE IS PRESENT..."

    file_path = os.path.join(curr_dir,user_file_name)
    print file_path
    FR = open(file_path,'r')
    #read_file = FR.read()
    #read_lines = read_file.split('\n')
    read_lines = FR.read().splitlines()


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
    cache_file_name[user_file_name]['if']=if_count
    cache_file_name[user_file_name]['for']=for_count

print cache_file_name


