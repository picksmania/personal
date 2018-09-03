import re

# Write a Python program to remove the parenthesis area in a string. Go to the editor
# Sample data : ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
# Expected Output:
# example
# w3resource
# github
# stackoverflow

'''
Sample_data = ["example (.com)", "w3resource", "github (.com)", "stackoverflow (.com)"]
for i in Sample_data:
    #print re.findall(r'\w+\s(\(.\w+\))',i)

    print re.sub(r'(\(.\w+\))', ' ',i)
'''

# Write a Python program to remove words from a string of length between 1 and a given number

'''
def remove_words(n):
    str = r'This is Prasit. He works in HPE. His wife is Rinki.The Sky is Blue'
    pat = r'\W*\b\w{1,3}\b'

    match = re.findall(pat,str)
    print match

    shortword = re.compile(r'\W*\b\w{1,3}\b')
    print(shortword.sub('', str))

remove_words(3)
'''

# Write a Python program to check a decimal with a precision of 2
'''
num = r'12.34 44.556 78.2345 34.54 11.23 44.6788'

pat = r'^\d+.[0-9]{1,2}'
pat1 = r'^[0-9]+(\.[0-9]{1,2})?$'

print re.findall(pat,num)
for m in re.finditer(pat,num):
    print m.group(),m.start(),m.end()
'''

# Write a Python program to do a case-insensitive string replacement.
'''
str = 'HE is a BOY. he lives in Heroshima. hE travel in Hero Bike'

pat1 = r'he|he(\w+)?'
#s = re.compile(pat,re.I)
print re.findall(pat1,str,re.I)
s = re.compile(pat1,re.I)
print s
n = s.sub('she',str,5)
print str
print "n::",n
'''

# Write a Python program to split a string at uppercase letters.
'''
str = 'PythonTutorialAndExercises'
pat = r'[A-Z][a-z]*'
print re.split(pat,str)
print re.findall(pat,str)
'''

# Write a python program to convert snake case string to camel case string.
# input = 'python_exercise'
# output = 'PythonExercise'

'''
str = 'python_exercise'
pat = r'\w+_.*'
pat1 = '(\w+)_(\w+)'
print re.findall(pat,str)
x =  re.findall(pat,str)
print type(x),x[0]
n = []
#print re.split(pat)
for i in x:
    s= i.split('_')
y = ''.join([i.capitalize() for i in s])
z = ''.join([i.upper() for i in s])
print y,z

'''

'''
with open(r'C:\STORCLI\output.txt','r') as fh:
    content = fh.read()
    #print content, type(content)
# print re.findall(r'Product Name = HPE.*',content)
# print re.findall(r'FW Version = (\d+.*){1,2}',content)
# print re.search(r'(FW Version = \d+.*)',content)
# print re.findall(r'Physical Drives = (\d+)',content)
drive_details = re.split('\n',content)
# print drive_details,type(drive_details)
# my_line = []
available_drive = {}
unavailable_drive = {}
available_drive_with_id = {}
available_drive_with_ctrl_slot = {}
unavailable_drive_with_ctrl_slot = {}

model_list = []
#drive_details_1 = re.split(' ',drive_details)
#print drive_details_1
with open(r'C:\one_off.txt') as f:
    model_list = f.read()
    final = model_list.split('\n')
    print "FINAL LIST:::",final
for i in drive_details:
    new_list = re.split(' ',i)
    for j in final:
        if new_list.__contains__(j):
            #print 'DRIVE FOUND'
            available_drive_with_id[j]=new[0]
            #available_drive_with_id[new[0]]=j
        # else:
        #     print 'NOT FOUND'
print available_drive_with_id
#     print drive_details[drive_details.index('Drive LIST')+10]
'''
# #print all_ctrl_details
# pat = 'Number of Controllers = (\d)'
# number_of_ctrl_found = re.findall(pat,all_ctrl)
# print number_of_ctrl_found,type(number_of_ctrl_found)
# numbers = [int(x) for x in number_of_ctrl_found]
# print numbers
# for i in range(0,numbers):
#     prin

onemodel = 'EO000800JWDKQ'
dict ={'0':' 246:5     6 JBOD  -  800.00 GB SAS  SSD N   N  512B EO000800JWDKQ    U  -'}
for k,v in dict.items():
    pat = '\d+:\d\s+.*.' + onemodel
    match = re.findall(pat, v)
    if match:
        print "MATCH FOUND"
    else:
        print "NOT FOUND"