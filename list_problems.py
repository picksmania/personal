# Write a Python program to sum all the items in a list.

# l = [10,20,30,40,50]
#
# list_sum = 0
# list_mul=1
'''
for i in range(0,len(l)):
  print l[i]
  list_sum= list_sum+l[i]
  list_mul = list_mul * l[i]
'''
# for i in l:
#     list_sum+=i
#     list_mul*=i
# print list_sum
# print list_mul

# ==============================================================================================

# Write a Python program to check if all dictionaries in a list are empty or not
# Sample list : [{},{},{}]
# Return value : True
# Sample list : [{1,2},{},{}]
# Return value : False

'''
def check_list(a):
    for i in a:
        print bool(i)
    print(all(not d for d in a))


check_list([{1,2},{},{}])
print "******************"
check_list([{},{},{}])
'''
# ==============================================================================================
# Write a Python program to get the depth of a dictionary

'''
def dict_depth(d, depth=1):
    if not isinstance(d, dict) or not d:
        return depth
    return max(dict_depth(v, depth+1) for k, v in d.iteritems())

s= dict_depth({'a':1, 'b': {'c': {'d': {}}}})

print s

'''
# ==============================================================================================
# Extend a list without append
'''
l = [10,20,30,40,50]
t = [11,22,33,44,55]
str ='abcde'
str1 = '12345'
print len(l)
l[len(l):] = t
print str[-4::-1]
print l

a = '123454321'
if a[::] == a[::-1]:
    print "Palindrom"
else:
    print "NOT PALIN"
'''
# ==============================================================================================
# Write a Python program to remove duplicates from a list of lists
# Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# New List : [[10, 20], [30, 56, 25], [33], [40]]

# import itertools
# sample_list = [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# new_list = []
'''
for i in sample_list:
    if i not in new_list:
        new_list.append(i)
print new_list
'''
'''
sample_list.sort()
new_num = list(num for num,_ in itertools.groupby(sample_list))
print("New List", new_num)
'''
# ===================================================================

# Write a Python program to find all the values in a list are greater than a specified number.

'''
def list_check(n,l):
    new_list = []
    for i in l:
        if i >n:
            new_list.append(i)

    print new_list
sample_list = [11,20,30,234,54,65,78,101]
list_check(50,sample_list)
'''
# sample_list = [11,20,30,234,54,65,78,101]
# new_list = []
# print (all(x>50 for x in sample_list))
# ========================================================================================

# Write a Python program to find the list in a list of lists whose sum of elements is the highest
# Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# Expected Output: [10, 11, 12]

# def list_of_list(*args):
#
#     print (max(*args,key=sum))
#
# list_of_list([1,2,3], [4,5,6], [10,11,12], [7,8,9])

# ========================================================================================

# Write a Python program to iterate over two lists simultaneously.
'''
list1 = [1,2,3,4]
list2 = ['a','b','c','d']

print zip(list1,list2)

print [(a, b) for (a,b) in zip(list1,list2)]
'''
# ========================================================================================

# Write a Python program to generate groups of five consecutive numbers in a list
'''
new_list = []

for i in range(5):
    for j in range(1,5):
        new_list.append(5*i+j)

print new_list
l = [[5*i + j for j in range(1,6)] for i in range(5)]
print l
'''
# ========================================================================================

# Write a Python program to split a list based on first character of word.
'''
word_list = ['be','have','do','say','get','make','go','know','take','see','come','think',
     'look','want','give','use','find','tell','ask','work','seem','feel','leave','call']

d = {}

for i in word_list:
    #print "***** %s ******"%(i)
    keys = d.keys()
    values = d.values()
    #print keys,values
    # print i[0]
    if i[0] not in keys:
        d[i[0]] = [i]
        # print d.keys()
        # print type(d.keys())
    else:
        #print "****** %s present in keys******"%i[0]
        d.setdefault(i[0],[]).append(i)

print d
'''
# ========================================================================================
# Write a Python program to convert a list of multiple integers into a single integer.
'''
L = [11, 33, 50]
print ("".join(map(str, L)))
print (lambda x:x**2,L)
print map(lambda x:x**2,L)
s = [x**2 for x in L]
print s
'''
# Map applies a function to all the items in an input_list. Here is the blueprint:
#
# map(function_to_apply, list_of_inputs)

# ========================================================================================


# Write a Python program to change the position of every n-th value with the (n+1)th in a list. Go to the editor
# Sample list: [0,1,2,3,4,5]
# Expected Output: [1, 0, 3, 2, 5, 4]
'''
import itertools
sample_list =[0,1,2,3,4,5]
new_list = []
s = sample_list[::2]
n = sample_list[1::2]
print s,n
print (zip(n,s))

print  "**************************************************************"
result = [None]*(len(s)+len(n))  # KEY STEPS to create a LIST of original list's size
print result
result[::2] = n
result[1::2] = s
print result

print  "**************************************************************"
iters = [iter(n), iter(s)]
print list(it.next() for it in itertools.cycle(iters))
'''

# Write a Python program to find common items from two lists
'''
color1 = "Red", "Green", "Orange", "White"
color2 = "Black", "Green", "White", "Pink"
print(set(color1) & set(color2))
'''

# Write a Python program to create a list by concatenating a given list which range goes from 1 to n. Go to the editor
# Sample list : ['p', 'q']
# n =5
# Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']
'''
sample_list = ['p','q']
new_list = []
n = 5
for i in range(1,n+1):
    for j in sample_list:
        new_num = j+str(i)
        new_list.append(new_num)

print new_list
print "************************************************"
new_list1 = ['{}{}'.format(x, y) for y in range(1, n+1) for x in sample_list]
print new_list1
'''
#

'''
original_list = [[2,4,3,4,5],[15,6,99], [9,10,11,12], [7,9,0]]
merged_list = []
for i in original_list:
    j = len(merged_list)
    merged_list[j:] = i[:]
print merged_list
print min(merged_list)
'''
# Fetch PRIME numbers from a given list
'''
num1= int(raw_input("Enter 1st Number:::"))
num2 =int(raw_input("Enter 2nd Number :::"))
for x in range(num1,num2):
    prime = True
    for i in range(2,x):
        if (x%i==0):
            prime = False
    if prime == True:
       print x

print "Done......"
'''

# MATRIX problem

'''
r = int(raw_input('enter the number of rows:::'))
c = int(raw_input('enter the number of column:::'))
M = []
print "enter elements"
for i in range(r):
  L = []
  for j in range(c):
      x= int(raw_input())
      L.append(x)
  M.append(L)
print "The given matrix is::"
for row in M:
  for x in row:
    print x,' ',
    print

'''
'''

a = [1,2,3,4,5]
b = [11,22,33,44,55]
c= [[1,2,3],[4,5,6],[7,8,9]]
print zip(a,b)
print zip(*c)
'''

'''
from heapq import nlargest
A = [100,22,44,555,678,987,568,199]
print sorted(A)
s = nlargest(3,A)
print s

'''
'''
from operator import add
l = [1,2,3,4,5]
m = [10,20,30,40,50]

s = map(add,l,m)
print s

k = zip(l,m)
print k
s = [sum(i) for i in k]
print s
'''

# Write a Python program to get the difference between the two lists
'''
l1 = [11,22,33,44,55,66,77,88]
l2 = [22,12,32,44,54,66,99,88]
new_list_common = []
new_list_unique = []
for i in l1:
    print type(i)
    if l2.__contains__(i):
        new_list_common.append(i)
    else:
        new_list_unique.append(i)

print "Unique:::",new_list_unique
print "Common::",new_list_common

print(list(set(l1) - set(l2)))

'''
'''
l =[1,2,3,4,5,9,2,2,3,4,10]
l.pop()
print l
print l.count(2)
l.reverse()
print l
l.sort()
print l
'''

l = [1,2,3,4,5,6]
s= len(l)
for i in range((len(l)-2),0,-1):
    print i











