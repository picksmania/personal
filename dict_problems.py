# Write a Python program to create a dictionary from two lists without losing duplicate values
'''
list1 = ['Class-V', 'Class-VI', 'Class-VII', 'Class-VIII', 'Class-V','Class-IV']
list2 = [1, 2, 2, 3, 7,8]
#list2 = ['a','b','c','d','e']

print dict(zip(list1,list2))
d = {}
for i in range(0,len(list1)):
    if list1[i] in d.keys():
        d[list1[i]] = [list2[i]]
       # print d.values()
    else:
        print list2[i]
        d.setdefault(list1[i],[]).append(list2[i])
        #print d.values()
print d
'''


###################################################################################################

# Write a Python program to sort Counter by value. Go to the editor
# Sample data : {'Math':81, 'Physics':83, 'Chemistry':87}
# Expected data: [('Chemistry', 87), ('Physics', 83), ('Math', 81)]
'''
sample_dict = {'Math':81, 'Physics':83, 'Chemistry':87}
print list(sample_dict.keys())
print list(sample_dict.values())
print zip(sample_dict.keys(),sample_dict.values())
'''

###################################################################################################

# Write a Python program to count number of items in a dictionary value that is a list.
'''
dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
ctr = sum(map(len, dict.values()))
ctr1 = min(map(len,dict.values()))
print ctr,ctr1
'''

###################################################################################################


# Write a Python program to print a dictionary line by line.

'''
students = {'Aex':{'class':'V',
        'rolld_id':2},
        'Puja':{'class':'V',
        'roll_id':5}}
print type(students)
for i in students:
    print i
    for j in students[i]:
        print j
        #print j,':',students[i][j]
        print j,'::',students[i][j]
print "*************************************************"
print students.items()
for i in students.iterkeys():
    print i,'>>',students.__getitem__(i)

'''
###################################################################################################
# Dict to LIST
'''
dict_num = {11: 10, 22: 20, 33: 30, 44: 40, 55: 50, 66: 60}
# for count,(k,v) in enumerate(dict_num.items(),1):
#     print "key",'   Value','  Count'
#     print k,'   ',v,'    ',count

list_num = list(dict_num.items())
print list_num
new_list = []
for i in list_num:
    for j in i:
        new_list.append(j)

print new_list
new_list2 = []
[new_list2.append(j) for i in list_num for j in i]
print new_list2

my_dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
s = map(len,my_dict.values())
print s

'''
###################################################################################################

# Write a Python program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
'''
Sample_dict = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

output = []
final= {}
for k,v in Sample_dict.items():
    output.append(v)
print output

s = sorted(output)
x = len(s)-3
top = s[x:]
print top
for i in top:
    for k,v in Sample_dict.items():
        if i == v:
            print k,'::',v
            final.setdefault(k,[]).append(v)

print final

print "***************************************************"
from heapq import nlargest
from operator import itemgetter
items = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
for name, value in nlargest(3, items.items(), key=itemgetter(1)):
    print(name, value)


print max(items.items())
'''
###################################################################################################

# Write a Python program to create and display all combinations of letters,
# selecting each letter from a different key in a dictionary. Go to the editor
# Sample data : {'1':['a','b'], '2':['c','d']}
# Expected Output:
# ac
# ad
# bc
# bd
'''
import itertools as it
d = {'1':['a','b'], '2':['c','d']}
allvalues = sorted(d.keys())
print allvalues
combinations = it.product(*(d[Name] for Name in allvalues))
final = list(combinations)
print final,type(final)
print ','.join(map(str,final))

for combo in it.product(*[d[k] for k in sorted(d.keys())]):
    print(''.join(combo))

'''

'''

import itertools
d = {'1':['a','b'], '2':['c','d'],'3':['e','f']}
l = [11,22,33,44,55,66]
q = 'AAAAAAABBBCCDDDEEFFF'
new = sorted(q)
print new
s = itertools.chain(d,l)
#m = itertools.chain(l)
print "s is::",s
for i in s:
    print i
print "***************************"
# for i in m:
#     print i

#
# o = itertools.combinations(d.values(),2)
# for i in o:
#     print i
#
# n = itertools.groupby(new)
# for i in n:
#     print i
'''
###################################################################################################

# a = ['a','b','c','d']
# b = ['m','n','o','p']
# s = zip(a,b)
# print zip(*s)

###################################################################################################
# Write a Python program to sort a dictionary by key.
'''
color_dict = {'red':'#FF0000',
          'green':'#008000',
          'black':'#000000',
          'white':'#FFFFFF'}

for key in sorted(color_dict):
    print("%s: %s" % (key, color_dict[key]))


print sorted(color_dict)
'''