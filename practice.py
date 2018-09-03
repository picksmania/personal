import os
import sys
import gc
import time
'''from datetime import datetime

mx = 2 * 10 ** 7
absloop = []
stime = datetime.now()
for n in range(mx):
    absloop.append(abs(n))

print "WORK done"
etime = datetime.now()-stime
print etime
##############################
class Myclass():
    pass
s = Myclass
print type(s)
print type(Myclass)
def a():
    pass
print type(a)'''

####################################
'''class Point():
    x=10
    y=20
p = Point()
p.x=30
p.z=40
print type(p)
print type(Point)
print "Class Attribute", Point.x
print "Class Attribute", Point.y
print "Instance Attribute", p.x
print "Instance Attribute", p.z
print id(p.x)
print id(Point.x)
#del p.x
#print p.x
print Point.x
#print p.__class__.__mro__
print Point.__module__.capitalize()'''
################################
'''
class A:
    label='a'
    pass
class B(A):
    label='b'
    pass
class C(A):
    label = 'c'
    pass
class D(B,C):
    pass
d=D()
print d.label
print d.__dict__.keys()
'''
'''
s = 'abcd123efg456'

for c in range(len(s)//2):
    #print s[c]
    print c,":",s[-c -1]
   # print s[c -1]
'''
'''
class A:
    def __init__(self, factor):
        self.__factor = factor
    def op1(self):
        print('Op1 with factor {}...'.format(self.__factor))

class B(A):
    def op2(self, factor):
        self.__factor = factor
        print('Op2 with factor {}...'.format(self.__factor))

class C(B):
    def op3(self, factor):
        self.__factor = factor
        print('Op3 with factor {}...'.format(self.__factor))

obj = C(100)
obj1 = C(1)
s = "i am the best"
print obj.op1()
print obj.op2(200)
print obj1.op3(800)
print obj.op1()
print obj.__dict__.keys()
print obj1.__dict__.keys()
print s.__len__()
'''
'''
import requests
import beautifulsoup4

def scrape(url, format_, type_):
    try:
        page = requests.get(url)
    except requests.RequestException as rex:
        print(str(rex))
    else:
        soup = BeautifulSoup(page.content, 'html.parser')
        images = _fetch_images(soup, url)
        images = _filter_images(images, type_)
        _save(images, format_)

        '''

## reverse file print
'''
for line in reversed(list(open(r'C:\Prasit\PRASIT1.txt','r'))):
    print(line)
print os.path.exists(r'C:\Prasit\PRASIT1.txt')
print os.path.isfile(r'C:\Prasit\PRASIT1.txt')
print os.path.isdir(r'C:\Prasit')
print os.path.getsize(r'C:\Prasit\PRASIT1.txt')
'''

## class variable vs instance variable
'''
class B():
    factor = 56
    def op2(self):
        #self.__factor = B.factor
        print('Op2 with factor {}...'.format(self.factor))
        op2_var = 100
        print('Op2 with op2_var {}...'.format(op2_var))
        print "CHanging the value of Factor..."
        B.factor = 60
        print('Op2 with factor {}...'.format(self.factor))
b = B()
c = B()
print "Object b is getting called\n\n"
b.op2()
print "\n\n"
print "Object C is getting called\n\n"
c.op2()
'''

'''
## append vs extend

a =[10,20,30]
b = [40,50,60]
c = [70,80,90]
d =[]
print "SIZE of a",a.__sizeof__()
print "SIZE of b",b.__sizeof__()
print "SIZE of c",c.__sizeof__()
print "SIZE of d",d.__sizeof__()
a.append(100)
b.extend(c)
print a
print b
print "SIZE of a",a.__sizeof__()
print "SIZE of b",b.__sizeof__()
print "SIZE of c",c.__sizeof__()

'''
### GENERATOR comprehension
'''
mygenerator = (x*x for x in range(3))
print type(mygenerator) # generator
for i in mygenerator:
    print i
print "1st time",mygenerator

mylist = [x*x for x in range(3)]
print type(mylist) # list
for i in mylist:
    print i


print "2nd time",mygenerator
for i in mygenerator:
    print i
for i in mylist:
    print i
for i in mylist:
    print i
'''

'''
## GENERATOR function
def createGenerator():
    mylist = range(3)
    #print mylist
    #print type(mylist)
    for i in mylist:
        yield i*i
mygen = createGenerator()
mygen2 = createGenerator()
print id(mygen)
print mygen2
for i in mygen:
    print i
print id(mygen2)
mygen2 = createGenerator()
print id(mygen2)
print mygen2.next()
print mygen2.next()
print mygen2.next()
#print mygen2.next()

'''

# print directory contents from top down approach
# traverse directory from top to bottom
'''
def directory_contents(path):
    # print os.listdir(path)
    if os.path.isdir(path):
        total = os.path.getsize(path)
        print "SIZE of %s is :: %s \n\n"%(path,total)
        #print path
        for subDir in os.listdir(path):
            # print "LIST DIR:::",subDir
            subDirPath = os.path.join(path,subDir)
            # print subDirPath
            # print os.path.isdir(subDirPath)
            if os.path.isdir(subDirPath):
                #pass
                directory_contents(subDirPath)
            else:
                #print(subDirPath)
                total_subdir = os.path.getsize(subDirPath)
                print (subDirPath),total_subdir
    else:
        print " '%s' path is not a directory"%path


path = directory_contents('C:\DSC\polls')
# path = directory_contents(r'C:\rewrite.txt')
# path = directory_contents('C:\TEST_tree')
'''

## Tree traversing using os.walk()
'''
for root, dirs, files in os.walk("C:\DSC\polls", topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
'''

# Binary Search -- must be on SORTED ARRAY
'''
def is_sorted(array):
    for i in range(1,len(array)):
        #print "ith element::", array[i]
        #print "i-1 th element::",array [i-1]
        if (array[i] < array[i-1]):
            #print "Array is NOT sorted"
            return False
    #print "Array is sorted"
    return True

#c = is_sorted(L)

def binSearch(array, elem):
    import time
    start = time.time()
    if not is_sorted(array):
        raise AssertionError("Elements are not in sorted order!")

    mid = len(array) // 2
    try:
        if array[mid] == elem:
            print "MATCH FOUND"
            end = time.time()-start
            print "It took %s time to complete binary search"%(end)
            return True
        elif (array[mid] < elem):
            return binSearch(array[mid+1:], elem)
        else:
            return binSearch(array[:mid], elem)
    except Exception as e:
        print "ELEMENT could not be found" ,e
    end = time.time()-start
    print "It took %s time to complete binary search"%(end)


L = [1,2,3,50,60,70,100,101,200,400,400,500,630,880]
b = binSearch(L,400)
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

c=time(0)
#print c
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



# draw an English Ruler
'''
def draw_line(tick_length, tick_label=''):
    line = '-' * tick_length
    if tick_label:
        line += ''+ tick_label
    print line
# c= draw_line(2)

def draw_interval(center_length):
    if center_length > 0: # stop when length drops to 0
        draw_interval(center_length-1) # recursively draw top ticks
        draw_line(center_length) # draw center tick
        draw_interval(center_length-1)

c = draw_interval(4)
'''

# check duplication in list without using set command
'''
def check_duplication(L):
    output = []
    for i in L:
        if i not in output:
            output.append(i)
    print output
    return output


list= [1,2,4,6,8,9,8,2,'prasit','bagal','rinki','bagal',1]
c=check_duplication(list)

'''

'''
# Summing the elements of a sequence using linear recursion

def linear_sum(S,n,l=0):
    if n == 0:
        return 0
    else:
        return linear_sum(S,n-1)+ S[n-1]



S = [1,2,3,4,5,6,7,8,9,10]
c=linear_sum(S,6)
print c
'''
# Reversing a Sequence with Recursion
'''
def reverse(S,start,stop):
    print "START INDEX:",start
    print "STOP INDEX:",stop-1
    if start < stop-1:
        print "Initial LIST::", S
        S[start], S[stop-1] = S[stop-1],S[start]
        print "Reverse LIST::", S
        reverse(S,start+1,stop-1)
    else:
        print "Closing the execution, as we Need more than ONE ITEM in the list to traverse"

S = [1,2,3,4,5,6,7,8,9,10,11]
# S = [1]
c = reverse(S,0,len(S))
'''

# LIST's length and size identification
'''
def list_size_check(n):
    import sys,time
    l =[]
    start = time.time()
    for i in range(n):
        a =len(l)
        b = sys.getsizeof(l)
        c = l.__sizeof__()
        print "Length: {0:3d}; Size in byte [getsizeof]: {1:4d}; Size in Byte [__sizeof__]: {2:4d}".format(a,b,c)
        l.append(None)
    end = time.time()
    time_taken= end - start
    #print l
    print time_taken/2

c = list_size_check(1000)

'''

'''
l = [1,2,3,4]
print "ID of L::",id(l)
print "Original ID of 0th location::",id(l[0])
print "Original ID of 1st location::",id(l[1])
print "Original ID of 2nd location::",id(l[2])
print "Original ID of 3rd location::",id(l[3])
print "appending one item..."
l.append(5)
print "ID of L::",id(l)
print "Original ID of 4th location::",id(l[4])
print "Inserting a new value at INDEX position 2..."
l.insert(2,10)
print "Original ID of 0th location::",id(l[0])
print "Original ID of 1st location::",id(l[1])
print "Original ID of 2nd location::",id(l[2])
print "Original ID of 3rd location::",id(l[3])
print "Original ID of 4th location::",id(l[4])
print "Original ID of 5th location::",id(l[5])

print l

'''









'''
print"================================="
print "****GARBAGE COLLECTOR****"
print gc.get_count()
print gc.get_referents(c)
print gc.collect(2)
'''


'''

def pattern_check(s):
    counter = 0
    for i in range(0,len(s)):
        # print s[i]
        if s[i].startswith(('(','{','[')):
            counter+=1
        else:
            counter = counter-1
    print counter
    if counter == 0:
        print "PFERFECT"
    else:
        print "WRONG"

s = ")(())(())"
c = pattern_check(s)

'''


# Use of Dictionary
'''
d = {1:'a',2:'b',3:'c',4:'d',5:'e'}
print type(d)
print "ID of DICT_D::",id(d)
print "1 as KEY ID:",id(d.__getitem__(1))
print "2 as KEY ID:",id(d.__getitem__(2))

new_dict = d.copy()
#print id(new_dict)
print "ID of DICT_new_dict::",id(new_dict)
print "1 as KEY ID:",id(new_dict.__getitem__(1))
print "2 as KEY ID:",id(new_dict.__getitem__(2))

print "SIZE of D::",d.__sizeof__()
print "SIZE of new_dict",new_dict.__sizeof__()
d.setdefault(6,'f')
print d
d.setdefault(6,'g')
print d
print "SIZE of D::",d.__sizeof__()
print hash('Python')
print hash('python')
print hash('PythoNN')
print hash('Python')
print "VALUE of 1.1:::",hash(1.1)
print "VALUE of 4504.1:::",hash(4504.1)
print hash(1.1) == hash(4504.1)

test = {1.1:'first',4504.1:'second'}
l = [6,7,8,9]
t = (11,22,33)
#print hash(l)
print test[1.1],test[4504.1]
#test.setdefault(t)
print test
key = 'somekey'
for i in l:
    test.setdefault("somekey",[]).append(i)
print test
test['prasit']='bagal'
print test
print gc.get_count()
#print gc.get_objects()
print gc.get_referents(d)
print gc.collect(1)
#exit(0)

value = d.viewkeys()
print value,type(value)

value_1 = d.has_key(1)
print value_1

print "GET 1st KEY VALUE::",d.get(1)
print "GET KEYS:::",d.keys()
print iter(d)
print "printing all ITEMS of dictionary::",d.items()
print d.iteritems()
l = [6,7,8,9]
str = 'rini'
my_dictionary = dict.fromkeys(l, 0)
print my_dictionary
print"=============================="
my_dictionary_1 = {}
for key in my_dictionary:
    print key
    #for i in range(len(str)):
    my_dictionary_1.update(key=key,value='r')
print my_dictionary_1
print d.get(key)
print l
l.pop()
print l

#print my_dictionary.pop(7)
print my_dictionary
print my_dictionary.popitem()
print my_dictionary
'''

# Counting letter in a string
'''
str = "abababeecddrr ffhihjkidlsplwma!!@#lsolasebczxdesxxcffrgorhfupoarntqlaosut"
letter_count = {}
for letter in str:
    letter_count[letter] = letter_count.get(letter,0)+1
print letter_count # raw counts of letter

letter_items = list(letter_count.items())

letter_items.sort()
print letter_items
print type(letter_items)

s = letter_count.iterkeys()
for i in s:
    print s.next()
for key in letter_count:
    k = letter_count.values()
print "K is", k

'''
# STRING to INT conversion without using int() method
# this has been executed with ord() method

'''
str = '456'
str1 = '789'
k = str.strip()
print k[0],k[1],k[2]
print type(k)
print "ord(0):::",ord('0')
print "ord(1):::",ord('1')
print "ord(4):::",ord('4')
a = (ord(k[0]) - ord('0'))*100
b = (ord(k[1])- ord('0'))*10
c = (ord(k[2]) - ord('0'))*1
# a = (ord(k[0]))*100
# b = (ord(k[1]))*10
# c = (ord(k[2]))*1

d = a+b+c
print d
print type(d)
k = str1.strip()
print k[0],k[1],k[2]
print type(k)
a = (ord(k[0]) - ord('0'))*100
b = (ord(k[1])- ord('0'))*10
c = (ord(k[2]) - ord('0'))*1
e = a+b+c

print "Addition of TWO String is %s"%(d+e)
print "Multiplication of TWO String is %s"%(d*e)
'''

# BINARY to INT conversion
'''
B = '0101'
print reversed(B)
c = sum(2**i for i, x in enumerate(reversed(B)) if x == '1')
#c = sum(2**i for i, x in enumerate(B) if x == '1')
print c


l = [1,2,3,4,5]
for i,x in enumerate(reversed(l)):
    print "Index is{0:2d}, Value is {1:2d}".format(i,x)
print len(l)

'''
# DECORATOR:
#=========================================================
# DEFINITION: a decorator is a function that takes another
# function and extends the behavior of the latter function
# without explicitly modifying it

# MULTIPLE DECORATOR:
# =========================================================
# In case of multiple decorator, they use a "wrapper" to decorate other decorator.
# so while calling the function, it would call something like this:
# decorator1(decorator2(some_func)) , Here position does matter
# ========================================================
'''
def decorator_1(f):
    def inner(*args,**kwargs):
        print ("*"*30) # 1. Control is here
        print ("%%%%%%%%%%%%%%") # 2. control is here
        output = f(*args,**kwargs) #3. call 2nd decorator
        print "^^^^^^^^^^^^^^^" # 9. Control is here
        print ("*"*30) #10. Control is here
        return output #11. finally return the output of original function
    return inner

def decorator_2(f):
    def inner(*args,**kwargs):
        import time
        stime = time.time()
        print "+++++++++++++++" #4. Control is here
        #f(*args,**kargs)
        output = f(*args,**kwargs) #5 execute the main function
        etime = time.time()
        #print "TIME TAKEN::",etime-stime # 6. control is here
        time_taken = etime-stime
        print(f.__name__, 'took:',time_taken )
        print "---------------" # 7. control is here
        return output # 8. return the output of original function to 1st Decorator
    return inner


#@decorator_1
#@decorator_2
#@decorator_func  # 1st Decorator
#@decorator_3
@decorator_1
@decorator_2# 2nd Decorator


def list_position():
    l = range(111115)
    for i,x in enumerate(l):
        print "Index is {0:2d}, Value is {1:2d}".format(i,x)
    # print len(l)
    #return l

list_position()
'''
#@decorator_func
#@decorator_time_calc
# def linear_sum(S,n):
#     if n == 0:
#         return 0
#     else:
#         return linear_sum(S,n-1)+ S[n-1]
#
# S = [1,2,3,4,5,6,7,8,9,10]
# linear_sum(S,5)
# #print c


# ITERTOOLS
'''
import itertools

S = 'HACK'
final_output = []
for i in xrange(1,len(S)+1):
    #final_output.append(i)
    output_combination = [x for x in itertools.combinations(S,2)]
    output_permutation = [x for x in itertools.permutations(S,2)]

print "COMBINATION::::",output_combination
print "======================================"
print "PERMUTATION:::",output_permutation
print "======================================"
list_1 = range(20)
list_2 = ['a','b','c','d','e','f','g']
print "*********** CHAIN ********************"
# The chain() function takes several iterators as arguments
# and returns a single iterator that produces the contents of all of them as though they came from a single sequence
print list(itertools.chain(list_1,list_2))
print "======================================"
print "*********** IZIP *********************"
# izip() returns an iterator that combines the elements of several iterators into tuples.
# It works like the built-in function zip(), except that it returns an iterator instead of a list
print list(itertools.izip(list_1,list_2))
print "======================================"
print "********** IMAP **********************"
# The imap() function returns an iterator that calls a function on the values in the input iterators,
# and returns the results. It works like the built-in map(), except that it
# stops when any input iterator is exhausted (instead of inserting None values to completely consume all of the inputs).
for i in itertools.imap(lambda x,y:(x,y,x*y),xrange(5),xrange(5,10)):
    print "%d * %d = %d"%i

print "======================================"

'''
'''
import copy
l = [1,2,3,4]
l1 = l
l2 = copy.copy(l)
l3 = copy.deepcopy(l)

print "***********************"
print "l value::",l
print "l id is::",id(l)
print "***********************"
print "l1 value::",l1
print "l1 id is::",id(l1)
print "***********************"
print "l2 value::",l2
print "l2 id is::",id(l2)
print "***********************"
print "l3 value::",l3
print "l3 id is::",id(l3)

l.append(20)
print "**** AFTER APPENDING 20 to l*******"
print "l value::",l
print "l id is::",id(l)
print "***********************"
print "l1 value::",l1
print "l1 id is::",id(l1)
print "***********************"
print "l2 value::",l2
print "l2 id is::",id(l2)
print "***********************"
print "l3 value::",l3
print "l3 id is::",id(l3)


l1.append(30)
print "**** AFTER APPENDING 30 to l1 *******"
print "l value::",l
print "l id is::",id(l)
print "***********************"
print "l1 value::",l1
print "l1 id is::",id(l1)
print "***********************"
print "l2 value::",l2
print "l2 id is::",id(l2)
print "***********************"
print "l3 value::",l3
print "l3 id is::",id(l3)

l2.append(300)
print "**** AFTER APPENDING 300 to l2 *******"
print "l value::",l
print "l id is::",id(l)
print "***********************"
print "l1 value::",l1
print "l1 id is::",id(l1)
print "***********************"
print "l2 value::",l2
print "l2 id is::",id(l2)
print "***********************"
print "l3 value::",l3
print "l3 id is::",id(l3)

l3.append(400)
print "**** AFTER APPENDING 400 to l3 *******"
print "l value::",l
print "l id is::",id(l)
print "***********************"
print "l1 value::",l1
print "l1 id is::",id(l1)
print "***********************"
print "l2 value::",l2
print "l2 id is::",id(l2)
print "***********************"
print "l3 value::",l3
print "l3 id is::",id(l3)

print "*****ID of each item in l*********"
for i in l:
    print id(i)

print "***********************"
print "*****ID of each item in l1*********"
for i in l1:
    print id(i)

print "***********************"
print "*****ID of each item in l2*********"
for i in l2:
    print id(i)

print "***********************"
print "*****ID of each item in l3 *********"
for i in l3:
    print id(i)

print "***********************"



l1 = [1,2,3]
print id(l1),id(l1[0]),id(l1[1]),id(l1[2])
print "*********************************"
l2 = copy.copy(l1)
print id(l2), id(l2[0]),id(l2[1]),id(l2[2])
l2.append(30)

print "*********************************"
l3 = copy.deepcopy(l1)
print id(l3), id(l3[0]),id(l3[1]),id(l3[2])
l3.append(40)
l3.__delitem__(0)
print l1
print l2
print l3
print l1

print id(l1),id(l1[0]),id(l1[1]),id(l1[2])
print "*********************************"
print id(l2), id(l2[0]),id(l2[1]),id(l3[2])
print "*********************************"
print id(l3), id(l3[0]),id(l3[1]),id(l3[2])
print "*********************************"
print id(l1),id(l1[0]),id(l1[1]),id(l1[2])
'''

'''
i =5
print id(i),i
j=5
print id(j),j
k =5
print id(k),k

j=6
print id(j),j

print id(j),j

m = 256
print id(m),m
n = 256
print id(n),n

o = 500
print id(o),o
p = 500
print id(p),p

l = [1,2,3,4]
L =l
print id(l),id(l[0])
print id(L), id(L[0])
'''


#************ file comparision*************
'''
same_content = []
different_content = []
with open(r'C:\netstat.txt','r') as FH:
    data = FH.readlines()

with open(r'C:\netstat_1.txt','r') as FH1:
    data1 = FH1.readlines()

for i in range(0,len(data)):
    for j in range(0,len(data1)):
        if data[i] == data1[j]:
           # print "SAME CONTENT"
            same_content.append((data[i],data[j]))
        else:
            #print "DIFFERENT CONTENT" \
             #     "netstat line:: %s and netstat_1 line %s"%(i,j)
            different_content.append((data[i],data[j]))

print same_content
'''