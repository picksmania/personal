
# *************** BEGINING OF LIST PROBLEM ****************

# Python Program to Find the Largest Number in a List without builtin function
# Python Program to Find the Second Largest Number in a List
'''
l = [11,32,-10,3,44,2,10,300,23,77]
sorted_list = []
print max(l)
while l:
    minimum = l[0]
    for i in l:
        if i < minimum:
            minimum=i
    sorted_list.append(minimum)
    l.remove(minimum)
print "SORTED LIST::",sorted_list
print "Largets Number::",sorted_list[-1]
print "Second Largest Number is::",sorted_list[-2]
'''
# Python Program to Put Even and Odd elements in a List into Two Different Lists
'''
l = [11,32,3,44,2,10,300,23,77]
odd_list = []
even_list =[]
for i in l:
    if i%2==0:
        even_list.append(i)
    else:
        odd_list.append(i)
print "EVEN LIST:::",even_list
print "ODD_LIST:::",odd_list
'''

# Python Program to Merge Two Lists and Sort it
'''
l1 = [11,22,2,33,4,3,56,76,30]
l2 = [22,43,11,25,54,67,6,4,88]
merged_list =[]
print "... NEED to MERGE two LIST..."
merged_list = l1[:]
len_l1 = len(l1)
merged_list[len_l1:]=l2
print merged_list
merged_list.sort()
print "SORTED LIST IS:::",merged_list
'''

# Python Program to Sort the List According to the Second Element in Sublist
'''
a=[['A',34],['B',21],['C',26],['D',1]]
print len(a)
for i in range(0,len(a)):
    print "i",i
    #print len(a)-i-1
    for j in range(0,len(a)-1):
        print "j",j
        if(a[j][1]>a[j+1][1]):
            # temp=a[j]
            # a[j]=a[j+1]
            # a[j+1]=temp
            a[j],a[j+1]=a[j+1],a[j]

print(a)
'''


# Python Program to Find the Second Largest Number in a List Using Bubble Sort
'''
a = [11,2,33,-2,44,66,4,60,1]
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

print a
print "SECOND LARGEST NUMBER IS::::",a[-2]
'''

# Python Program to Sort a List According to the Length of the Elements

'''
a = ['cat','dog','goat','am','elephant','prasit','arabinda']
a.sort(key=len)
print a

for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if(len(a[j])>len(a[j+1])):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print a

'''

# Python Program to Create a List of Tuples with the First Element as the Number and Second Element as the Square of the Number
'''
s_num = int(raw_input("Enter the starting number..."))
e_num = int(raw_input("Enter the ending number..."))

a = [(x,x*x)for x in range(s_num,e_num+1)]
print a
'''

# Python program to Sort a List of Tuples in Increasing Order by the Last Element in Each Tuple
'''
# a = [(2,5),(1,2),(4,4),(2,3)]
a = [(23,45),(25,44),(89,40)]
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if(a[j][1])>(a[j+1][1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp
print a
'''

# Python Program to Read a file and count the occurence of one word
'''
with open(r'C:\downgrade.txt','r') as f:
    data_list = f.readlines()
print data_list, len(data_list)
count_linux = 0
count_esxi = 0
for i in data_list:
    if i.__contains__('Linux'):
        count_linux+=1
    elif i.__contains__('ESXi'):
        count_esxi+=1

print "LINUX COUNT %s and ESXI count %s"%(count_linux,count_esxi)
'''

# Python program to READ a file and fetch the hostname:ip address for all available host's in the file
'''
with open(r'C:\host_detail.txt','r') as f:
    data_list = f.read().splitlines()
    print type(data_list)
    print type(data_list[0])
d = {}
for i in data_list:
    if i.startswith('hostname'):
        server_name = i.split(' ')
    elif i.startswith('hostip'):
        ip_address = i.split()
        d.setdefault(server_name[2],[]).append(ip_address[2])

print d
'''
'''
flashed_string = [('firmware-hdd-0a38b25661-HPD3-2.1.x86_64.rpm', ''), ('firmware-hdd-1cbab97ff0-HPD5-2.1.x86_64.rpm', ''), ('firmware-hdd-2e4c61fc63-HPD3-3.1.x86_64.rpm', ''), ('firmware-hdd-3ab4c70e64-HPG4-3.1.x86_64.rpm', ''), ('firmware-hdd-3d97759111-HPD3-2.1.x86_64.rpm', ''), ('firmware-hdd-5d9e841607-HPD3-2.1.x86_64.rpm', ''), ('firmware-hdd-693b9a2853-HPD2-2.1.x86_64.rpm', ''), ('firmware-hdd-71af849f3b-HPD3-2.1.x86_64.rpm', ''), ('firmware-hdd-7505dfb5ae-HPD6-2.1.x86_64.rpm', ''), ('firmware-hdd-7c1a1734f9-HPD2-2.1.x86_64.rpm', ''), ('firmware-hdd-8c4a212ff9-HPD4-3.1.x86_64.rpm', ''), ('firmware-hdd-8ed8893abd-HPD6-2.1.x86_64.rpm', ''), ('firmware-hdd-a2d4b5c742-HPG1-3.1.x86_64.rpm', ''), ('firmware-hdd-ac3fda26eb-HPD6-3.1.x86_64.rpm', ''), ('firmware-hdd-ec908c3650-HPG5-2.1.x86_64.rpm', ''), ('firmware-hdd-edf6dcd906-HPD6-2.1.x86_64.rpm', '')]

final_list = []
s = [i[0] for i in flashed_string]
#print s,len(s)

with open(r'C:\new_test_rpm\sum_log.txt','r') as f:
    data_list = f.read().splitlines()
#print data_list
d = {}
for i in data_list:
    if i.startswith('Component Filename'):
        component_name = i.split(':')
    elif i.startswith('Component Name'):
        drive_model = i.split(':')
        #print drive_model
        d.setdefault(drive_model[1],[]).append(component_name[1])

print d
'''


#updated = ['firmware-hdd-0a38b25661-HPD3-2.1.x86_64.rpm','firmware-hdd-1cbab97ff0-HPD5-2.1.x86_64.rpm','firmware-hdd-2e4c61fc63-HPD3-3.1.x86_64.rpm','firmware-hdd-3ab4c70e64-HPG4-3.1.x86_64.rpm','firmware-hdd-3d97759111-HPD3-2.1.x86_64.rpm', 'firmware-hdd-5d9e841607-HPD3-2.1.x86_64.rpm','firmware-hdd-693b9a2853-HPD2-2.1.x86_64.rpm','firmware-hdd-71af849f3b-HPD3-2.1.x86_64.rpm','firmware-hdd-7505dfb5ae-HPD6-2.1.x86_64.rpm','firmware-hdd-8c4a212ff9-HPD4-3.1.x86_64.rpm','firmware-hdd-8ed8893abd-HPD6-2.1.x86_64.rpm','firmware-hdd-ac3fda26eb-HPD6-3.1.x86_64.rpm','firmware-hdd-ec908c3650-HPG5-2.1.x86_64.rpm', 'firmware-hdd-edf6dcd906-HPD6-2.1.x86_64.rpm']
#print type(updated)
import os
# import glob, os
# parent_dir = r"C:\new_test_rpm"
# l=[]
# for rpm_file in glob.glob(os.path.join(parent_dir, '*.rpm')):
#     print (rpm_file),type(rpm_file)
#     print rpm_file.split('\\')
#
# l1 = [11,22,33,44,55,66,77]
# l2 = [22,33,77]
# l4 = ['abc','def','ijkl']
# l3 = list(set(l1)-set(l2))
# print l3
# print type(l4[0])




# ************  END OF LIST PROBLEMS *******************************


# *************** BEGINNING OF STRING PROBLEM ****************
# replace a with $
'''
str1 = 'apple cat mat sky hifi App Elephant'
for i in str1:
    if i == 'a':
        str2 = str1.replace(i,'$')
print str2
'''

# ***************** RECURSION ***************************

# factorial
'''
def fact(n):
    if n<=1:
        return 1
    else:
        return  n*fact(n-1)

result = fact(6)
print result

'''
'''
def fibo(n):
    if n<=1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

result = fibo(10)
print result
'''
# Python Program to Find the Sum of Elements in a List Recursively
'''
def sum_arr(arr,size):
   if (size == 0):
     return 0
   else:
     retursize-n arr[1] + sum_arr(arr,size-1)
n=int(input("Enter the number of elements for list:"))
a=[]
for i in range(0,n):
    element=int(input("Enter element:"))
    a.append(element)
print("The list is:")
print(a)
print("Sum of items in list:")
b=sum_arr(a,n)
print(b)
'''
'''
def sum_of_list(a):
    if len(a) == 0:
        return 0
    else:
        #return a[0]+sum_of_list(a[1:])
        return a[0]+sum_of_list(a[1:])
a = [1,2,3,4,10]
b = sum_of_list(a)
print b
'''
'''
import os
for root, dirs, files in os.walk("C:\Component_logs\Actual", topdown=True):
    for name in files:
        print(os.path.join(root, name))
        path = (os.path.join(root, name))
        with open(path,'r') as f:
            data = f.read().splitlines()
            for line in data:
                if line.__contains__('Cancelled queued flashes'):
                    print path
'''
'''
for root, dirs, files in os.walk("C:\Component_logs\Actual", topdown=True):
    for name in files:
        print(os.path.join(root, name))
    for name in dirs:
        print(os.path.join(root, name))
'''

# A string will become a PALINDROM, if you remove one CHAR from given string.
# need to find out that CHAR's INDEX.

'''
s = 'ABCDEFGHIJKLMNOP'
y = len(s)
# print y,type(y)
print "s", s
print "S[1:]",s[1:] #BCD
print "s[-1:]",s[-1:]
print "s[:-1]",s[:-1]#ABC
print "s[::-2]",s[::-2]
print "s[-2:]",s[-2:]
print "s[::-1]",s[::-1]
print "********************************"
print "s[1::]",s[1::]
print "s[1::-1]",s[1::-1]
print "s[-1:0:-1]",s[-1:0:-1] # DCB
print "s[-2::-1]",s[-2::-1] #CBA
'''
'''
n=int(raw_input())
for n0 in range(n):
    s=list(raw_input())
    if list(reversed(s))==s:
        print -1
    else:
        for _ in range(1,(len(s)/2)+1):
            print "** _ **",_
            print s[1-1]
            print "** s[_-1] **",s[_-1]
            print "** s[-_] **",s[-_]
            if s[_-1]!= s[-_]:
                break
        s1=s[:]
        print s1
        print s
        print s[_-1]
        del s[_-1]
        del s1[-_]
        if list(reversed(s))==s:
            print _-1
        else:
            print len(s)+1-_
'''
'''
S= 'hgygsvlfcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcwflvsgygh'
#S ='baa'
i=0
for j in range(0,len(S)+1):
    s = S[:i] + S[i + 1:]
    if s[::]==s[::-1]:
        print "FOUND PALINDROM at pos %s"%i
        break
    else:
        i+=1
'''

# Shallow Copy vs Deep Copy
import copy
a = [[1,2,3,[23]],4,5,6,['a','b','c']]
b = a
c = copy.copy(a)
d = copy.deepcopy(a)


print "a:%s |ID of a:%s | a[0]:%s | ID of a[0]:%s | ID of a[-1]:%s"%(a,id(a),a[0],id(a[0]),id(a[-1]))
print "b:%s |ID of b:%s | b[0]:%s | ID of b[0]:%s | ID of b[-1]:%s"%(b,id(b),b[0],id(b[0]),id(b[-1]))
print "c:%s |ID of c:%s | c[0]:%s | ID of c[0]:%s | ID of c[-1]:%s"%(c,id(c),c[0],id(c[0]),id(c[-1]))
print "d:%s |ID of d:%s | d[0]:%s | ID of d[0]:%s | ID of d[-1]:%s"%(d,id(d),d[0],id(d[0]),id(d[-1]))

print "****************************************************"
print "APPENDING elements to b, c and d...."
b.append(100)
c.append(200)
d.append(300)
print "****************************************************"
print "a:%s |ID of a:%s | a[0]:%s | ID of a[0]:%s | ID of a[-1]:%s"%(a,id(a),a[0],id(a[0]),id(a[-1]))
print "b:%s |ID of b:%s | b[0]:%s | ID of b[0]:%s | ID of b[-1]:%s"%(b,id(b),b[0],id(b[0]),id(b[-1]))
print "c:%s |ID of c:%s | c[0]:%s | ID of c[0]:%s | ID of c[-1]:%s"%(c,id(c),c[0],id(c[0]),id(c[-1]))
print "d:%s |ID of d:%s | d[0]:%s | ID of d[0]:%s | ID of d[-1]:%s"%(d,id(d),d[0],id(d[0]),id(d[-1]))

a[0]='AAA'

print a
print c

# my_list = [1, 3, 6, 10]
# a = (x**2 for x in my_list)
# print a.next()
# print a.next()
#
# def Foo(n):
#     def multiplier(x):
#         return x * n
#     return multiplier
#
# a = Foo(5)
# b = Foo(5)
#
# print(a(b(2)))