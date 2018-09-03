'''

class Rectangle:
    count = 0
    def __init__(self,x,y):
        self.length = x
        self.width = y

    def __str__(self):
        return "Rectangle({0},{1})".format(self.length,self.width)

    def area(self):
        return self.length * self.width

    def scale(self,len=0,wid=0):
        new_len = self.length+len
        new_wid = self.width + wid
        print "NEW_length::",new_len
        print "NEW_width::",new_wid
        return new_len*new_wid

    def __add__(self,other):
         t = Rectangle(self.length+other.length,self.width+other.width)
         return t

    def __eq__(self,other):
        if self.area() == other.area():
            print "SAME"
        else:
            print "NOT SAME"

    @classmethod
    def getcount(cls):
        return Rectangle.count

r1 = Rectangle(3,4)
print r1
print r1.area()
r2 = Rectangle(3,4)
print r2
print r2.area()
c = r1.scale(10)
print c
r3 = r1+r2
print r3
if r1==r2:
    print "same"
else:
    print "nt same"

'''
# ========================================================================================================
'''
import re
class IPaddress():
    def __init__(self,ip):
        self.ipadd = ip

    def __str__(self):
        return "IPAddress is({0})".format(self.ipadd)

    def isvalid(self):
        flag = True
        L = self.ipadd.split('.')
        if len(L) != 4:
            print "NOT VALID IP"
            flag=False
            return False
        else:
            for x in L:
                if not x.isdigit():
                    print "NOT VALID IP"
                    flag=False
                    return False
                else:
                    x = int(x)
                    if x<1 or x>255:
                        print "NOT VALID IP"
                        flag=False
                        return False
            else:
                if flag == True:
                    pat = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
                    if re.match(pat,self.ipadd):
                        print "VALID IP"
                        return True
                    else:
                        print "INVALID IP"
                        return False

    def __eq__(self,other):
        if self.ipadd == other.ipadd:
            return True
        else:
            return False

ip1 = IPaddress('11.22.33.44')
print ip1
c =ip1.isvalid()

ip2 = IPaddress('11.22.33.44')
print ip2
d = ip2.isvalid()

if ip1 == ip2:
    print "IP1 and IP2 are same IP"
else:
    print "IP1 and IP2 are Different IP"

'''

# ==========================================================================================

'''
class Matrix():
    def __init__(self,filepath1,filepath2):
        self.mat1 = filepath1
        self.mat2 = filepath2

    def __str__(self):
        return "Matrix 1 is{0} and Matrix 2 is{1}".format(self.mat1,self.mat2)

    def getdata(self):
        fh = open(self.mat1,'r')
        mat1_data = fh.read().splitlines()
        fh.close()

        fh = open(self.mat2,'r')
        mat2_data = fh.read().splitlines()
        fh.close()


        return mat1_data, mat2_data

    def addtion(self):
        mat1_data,mat2_data = self.getdata()
        print type(mat1_data),type(mat2_data)
        print "MAT1 data:::",mat1_data
        print "MAT2_data:::",mat2_data
        a = []
        b = []
        for i in mat1_data:
            c = i.split(',')
            a.append(c)
        print a
        for i in mat2_data:
            c = i.split(',')
            b.append(c)
        print b

        a1 = [[int(x) for x in row] for row in a]
        print a1
        b1 = [[int(x) for x in row] for row in b]
        print b1

        result = [[0,0,0],[0,0,0],[0,0,0]]
        for i in range(len(a1)):
            for j in range(len(a1[0])):
                result[i][j]=a1[i][j]+b1[i][j]

        for r in result:
            print r


obj = Matrix(r'C:\Prasit\mat1.txt',r'C:\Prasit\mat2.txt')
print obj
obj.addtion()

'''
# ====================================================================================================
# Inheritance
'''
class Person:
    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return "Person Details ({0},{1},{2})".format(self.fname,self.lname,self.email)

    def fullname(self):
        return self.fname+ ' ' + self.lname

    def getemail(self):
        return self.email

class Employee(Person):
    def __init__(self,fname,lname,email,eid,salary):
        Person.__init__(self,fname,lname,email)
        self.eid =eid
        self.salary = salary

    def __str__(self):
        return "Employee Details ({0},{1},{2},{3},{4})".format(self.fname,self.lname,self.email,self.eid,self.salary)

    def getSalary(self):
        return self.salary

    def getemail(self):
        return self.email


p=Person('prasit','bagal','prasit.bagal@hpe.com')
print p

emp=Employee('krish','kayal','krish.kayal@pmc.com',123,1000)
print emp
print emp.getemail()
print emp.getSalary()

'''
# ===================================================================
'''
def f():
    print "HI"

def f(m):
    print "HELLO"

f()
'''
# ==========================================================================
# MRO:
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
# ==========================================================================
# Module:

'''
version = 2.3
l =[10,20,30]

def sample():
    return "HELLO"

class Rectangle:
    count = 0
    def __init__(self,x,y):
        self.length = x
        self.width = y

    def __str__(self):
        return "Rectangle({0},{1})".format(self.length,self.width)

    def area(self):
        return self.length * self.width

    def scale(self,len=0,wid=0):
        new_len = self.length+len
        new_wid = self.width + wid
        print "NEW_length::",new_len
        print "NEW_width::",new_wid
        return new_len*new_wid

    def __add__(self,other):
         t = Rectangle(self.length+other.length,self.width+other.width)
         return t

    def __eq__(self,other):
        if self.area() == other.area():
            print "SAME"
        else:
            print "NOT SAME"

    @classmethod
    def getcount(cls):
        return Rectangle.count



class Person:
    def __init__(self,fname,lname,email):
        self.fname = fname
        self.lname = lname
        self.email = email

    def __str__(self):
        return "Person Details ({0},{1},{2})".format(self.fname,self.lname,self.email)

    def fullname(self):
        return self.fname+ ' ' + self.lname

    def getemail(self):
        return self.email

class Employee(Person):
    def __init__(self,fname,lname,email,eid,salary):
        Person.__init__(self,fname,lname,email)
        self.eid =eid
        self.salary = salary

    def __str__(self):
        return "Employee Details ({0},{1},{2},{3},{4})".format(self.fname,self.lname,self.email,self.eid,self.salary)

    def getSalary(self):
        return self.salary

    def getemail(self):
        return self.email

'''

# ========================================================================================================

# write a script to compute TIME it takes to fill a square matrix of order N randonly with random Values in the range 1 to 1000 with CLI interface
'''
from datetime import datetime
import random
import sys

if len(sys.argv) <2:
    print 'I need minimum 1 input file names...'
    sys.exit(1)

stime = datetime.now()

input_data = sys.argv[1]

r = int(input_data)
c = int(input_data)
initial_value =0
print " We are going to crate a %s x %s MATRIX"%(r,c)
print "********Creating Matrix with default Value 0*******"
M =[]
i=0
while i<r:
    l =[] # this is to create ROW of matrix.
    j=0
    while j<c:
        l.append(initial_value)
        j=j+1   # going to create NEXT column
    M.append(l) # one ROW got created and inserted in main MATRIX which is M here
    i=i+1 # going to create NEXT ROW

print "The MATRIX is::::"
for row in M:
    for x in row:
        print x,
    print


print ".....Getting RANDOM NUMBER to fill up the MATRIX....."
item_to_be_inserted = r * c
print "Item_to_be_inserted::",item_to_be_inserted
hit_count =0
miss_count = 0
k=0
miss_matrix ={}
# for i in range(0,r+100):
#     for j in range(0,c+100):
#         row = random.randrange(0,r)
#         col = random.randrange(0,c)
        #print "Row %s and Column %s"%(row, col)


while k<item_to_be_inserted:
    row = random.randrange(0,r)
    col = random.randrange(0,c)

    for item in range(len(M)):
        for item1 in range(len(M[0])):
            value = random.randrange(1,1000)
            if M[row][col] == 0:
                M[row][col]= value
                hit_count+=1
                k+=1
                if hit_count==item_to_be_inserted:
                    break
            else:
                if miss_matrix.has_key(M[row][col]):
                    miss_matrix[M[row][col]]+=1
                else:
                    miss_matrix[M[row][col]]=1
                miss_count+=1
                continue

print "HIT COUNT",hit_count
print "MISS count",miss_count
print miss_matrix
sum_of_val=0
for k,v in miss_matrix.items():
    sum_of_val+=v
print sum_of_val


print "********* THE FINAL MATRIX **********"

for row in M:
    for x in row:
        print x,
    print

etime = datetime.now()

print "**************************************************"
print "Time TAKEN to create Default Matrix is %s"%(etime-stime)


'''
#===================================================================
# lambda, map, filter
'''
l1 = [1,2,3,4,5]
l2 = [10,20,30,40,50]
add = lambda a, b: a+b
map_val = map(add,l1,l2)
print map_val


# Need to find out SUM of square of (current+next item) in a list
val = reduce(add,[y*y for y in [(lambda x: x+(x+1))(x) for x in range(1,len(l1)+1)]])
print val

sq = [x*x for x in l1]
print sq

more_than_thirty = lambda x:x>30
filter_val = list(filter(more_than_thirty,map_val))
print filter_val
'''
#==============================================================================================

# PRIME CHECK

'''
for i in range(1,10):
    flag= True
    for x in range(2,i):
        print "NOW i is:::::",i
        print "NOW x is:::::",x
        if i%x==0:
            flag=False
            break
    if flag == True:
        print "PRIME NUMBER",i
'''
# for x in range(1,100):
#     prime = True
#     for i in range(2,x)
#         if (x%i==0):
#             prime = False
#     if prime == True:
#        print x

# =====================================================================
'''
l1 =[[1,2,3],[4,5,6]]
l2 = [[10,20,30],[40,50,60]]

s1 = zip(l1,l2)
s2 = zip(*l2)

print sum(s1)
print s2
'''