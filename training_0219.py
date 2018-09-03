import re

# write a script to count number of words in a given string.
'''
pra = 'Prasit is a boy. He lives in Bangalore. He is from Kolkata'
d ={}
pra_list = pra.split(' ')
#print pra_list
for x in pra_list:
    if x in d.keys():
         d[x]+=1
    else:
        d[x]=1
print d
'''

#####################################################################################

# write a script to compare 2 integers and add 10 to the smallest, add 20 to the biggest
'''
x = int(raw_input("plz insert 1st number..."))
y = int(raw_input("Plz insert 2nd number..."))

if x>y:
    print "%s is the biggest number.."%x
    x+=20
    y+=10
else:
    print "%s is the biggest number.."%y
    x+=10
    y+=20
print x,y

'''
###########################################################################

# write a script to remove all the duplicate words from a string.

'''
def unique_list(l):
    ulist = []
    [ulist.append(x) for x in l if x not in ulist]
    print ulist
    return ulist

#a = "calvin klein design dress calvin klein"
a ="Prasit is a boy. He lives in Bangalore. He is from Kolkata"
print a.split()
a =' '.join(unique_list(a.split()))
print a

'''
########################################################################################
# write a script to count the number of even length words along with the position from a string.
'''
str = 'write a script to count the number of even length words along with the position from a string'
l = str.split(' ')
for i,x in enumerate(l):
    if len(x)%2==0:
        print "Position {0:2d} and word {1:20s}".format(i,x)

'''

################################################################################################

# write a script to test a given IP is valid or not.
'''
s = raw_input("Enter an IP...")

pat = '^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'
if re.match(pat,s):
    print "VALID IP"
else:
    print "INVALID IP"
'''


#######################################################################################

# a =[10,20,30]
# b = [40,50,60]
# c = [70,80,90]
# d =[]
# print "SIZE of a",a.__sizeof__()
# print "SIZE of b",b.__sizeof__()
# print "SIZE of c",c.__sizeof__()
# print "SIZE of d",d.__sizeof__()
# a.append(100)
# b.extend(c)
# print a
# print b
# print "SIZE of a",a.__sizeof__()
# print "SIZE of b",b.__sizeof__()
# print "SIZE of c",c.__sizeof__()

# write a script to compare to TWO string of same length and give position where it's not SAME>
'''
str = 'It is a dog'
str1 = 'It is a goat'
print len(str),len(str1)
a = str.split(' ')
b = str1.split(' ')
print a,b

if len(str) != len(str1):
    elem1 = [x for x in str.split()]
    elem2 = [x for x in str1.split()]

    for pos,item in enumerate(elem1):
        if item not in elem2:
            print "POSITION where it dint match is: %s and value is %s"%(pos,item)
'''

# write a script to read and display MATRIX.

# mat1 =[]
# mat2 =[]
# first_row = []
# second_row =[]
#
# third_row =[]
# fourth_row =[]
#
# x = int(raw_input("Enter the Number of Rows in 1st matrix...."))
# y = int(raw_input("Enter the Number of column in 1st matrix...."))
# for i in range(0,x):
#     #first_row.append(int(raw_input("Enter the values in 1st row....")))
#     for j in range(0,y):
#         first_row.append(int(raw_input("Enter the values in 1st row....")))
#     #second_row.append(int(raw_input("Enter the values in 2nd row....")))
#
#
# print first_row,second_row

# u = int(raw_input("Enter the Number of Rows in 2nd matrix...."))
# v = int(raw_input("Enter the Number of column in 2nd matrix...."))
#
# for i in range(0,u):
#     third_row.append(int(raw_input("Enter the values in 1st row....")))
# for i in range(0,v):
#     fourth_row.append(int(raw_input("Enter the values in 2nd row....")))
#
# print third_row,fourth_row
#
#
# mat1.append(first_row)
# mat1.append(second_row)
# mat2.append(third_row)
# mat2.append(fourth_row)
#
#
# result = [[0,0,0],[0,0,0],[0,0,0]]
# for i in range(len(mat1)):
#     for j in range(len(mat1[0])):
#         #print mat1[i][j]
#         #print mat2[i][j]
#         result[i][j]=mat1[i][j]+mat2[i][j]
#
# for r in result:
#     print r
#


r = int(raw_input("Enter the Number of Rows in 1st matrix...."))
c = int(raw_input("Enter the Number of column in 1st matrix...."))

print "Enter Data::::"
M =[]
i=0
while i<r:
    l =[]
    j=0
    while j<c:
        x =int(raw_input(" enter value...."))
        l.append(x)
        j=j+1
    M.append(l)
    i=i+1

print "The MATRIX is::::"
for row in M:
    for x in row:
        print x,
    print
