'''
def solveMeFirst(a,b):
   # Hint: Type return a+b below
    return a+b


num1 = input()
num2 = input()
res = solveMeFirst(num1,num2)
print res
'''

'''
l = [1,2,3,4,5]
sum = 0
for i in l:
    sum=sum+i
print sum
'''

# triplet
'''
def solve(a0, a1, a2, b0, b1, b2):
    A=0
    B=0
    a = [a0,a1,a2]
    b = [b0,b1,b2]
    for i in range(3):
        if a[i]>b[i]:
            A+=1
        elif a[i]<b[i]:
            B+=1
    print A,B

solve(1,2,63,11,11,31)
'''
# LONG SUM
'''
a = [1000000001,1000000002,1000000003,1000000004,1000000005]
sum = 0
for i in a:
    sum=sum+i
print sum
'''

# Complete the diagonalDifference
'''
a = [[11,2,40],[4,5,6],[10,8,-12]]
primary = []
secondary = []
for row in a:
    for x in row:
        primary.append(x)
print primary
x = primary[0]+primary[4]+primary[-1]
y = primary[2]+primary[4]+primary[-3]
print abs(x-y)
'''

# matrix
# Complete the diagonalDifference
'''
n = int(raw_input("Please enter the matrix level"))
M=[]
i=0
r=c=n

while i<r:
    l= []
    j=0
    while j<c:
        x = int(raw_input("Enetr Value:::"))
        l.append(x)
        j+=1
    M.append(l)
    i+=1

print "Matrix is:::"
for row in M:
    for x in row:
        print x,
    print

print len(M)

i =0
j =-1
k = 0
x = []
y = []
while i<len(M):
    x.append(M[i][j])
    y.append(M[i][k])
    j-=1
    k+=1
    i+=1
print x
print y
sum_x =0
sum_y =0
for i in x:
    sum_x = sum_x+i
for i in y:
    sum_y = sum_y+i

print abs(sum_x-sum_y)
'''

# check the proportion of positive,negiative and zero in a list
'''
M = [1,2,0,-2,0,0,-44,2,-3,33,-88]
print len(M)
positive=0
negative =0
zero =0
for i in M:
    if i>0:
        positive+=1
    elif i <0:
        negative+=1
    elif i==0:
        zero+=1
    else:
        print "Its not a digit.."

pos_percentage = positive/float(len(M))
neg_percentage = negative/float(len(M))
zero_percentage = zero/float(len(M))


print ("%.6f"%pos_percentage)
print ("%.6f"%neg_percentage)
print ("%.6f"%zero_percentage)
'''

# A single integer, denoting the size of the staircase.
'''
chr = '#'
space = ' '
n =6
j=1
for i in range(1,n+1):
    print space*(n-j)+chr*i
    j+=1
'''

# max n min
'''
m = [1,2,3,4,50]
data = []
print sum(m[1:])
print sum(m[:-1])
for i in range(0,len(m)):
    print i
    data.append(sum(m[:])-m[i])
print data
print max(data),min(data)
'''

# birthday cake candle
'''
n=5
a = [2,3,3,4,1]
for i in range(0,len(a)):
    for j in range(0,len(a)-1):
        if(a[j]>a[j+1]):
            temp=a[j]
            a[j]=a[j+1]
            a[j+1]=temp

height=a[-1]
print height


count= 0
for i in a:
    if i==height:
        count+=1
print count
'''

# time conversion:
# Sample Input 0
#
# 07:05:45PM
# Sample Output 0
# 19:05:45
'''
def timeConversion(s):
    try:
        l = s.split(':')
        print l
        hour = l[0]
        min = l[1]
        sec = l[2]

        for i in range(0,len(l)-1):
            if len(l[i])>2:
                #print l[i]
                print "Incorrect TIME FORMAT.."
                return None
            elif not l[i].isdigit():
                print "TIME SHOULD BE IN DIGIT format"
                return None
            #break
        if len(sec)>4:
            print "Incorrect TIME FORMAT in seconds"
            return None

        new_sec = sec[:2]
        if not new_sec.isdigit():
            print "Incorrect TIME FORMAT in seconds"
            return None

        if (int(hour)<0) or (int(new_sec)<0) or (int(min)<0):
                print "NEGATIVE TIME IS NOT ALLOWED..."
                exit()
        if s.endswith('PM'):
            if int(hour)==12:
                new_time = hour +':'+min + ':'+new_sec
            elif int(hour)< 12 and int(hour)>0:
                n_hour = int(hour)+12
                new_time = str(n_hour) +':'+min + ':'+new_sec
            print new_time
            return new_time

        elif s.endswith('AM'):
            if int(hour)==12:
                new_time = '00' +':'+min + ':'+new_sec
            elif int(hour)< 12 and int(hour)>9:
                n_hour = int(hour)
                new_time = str(n_hour) +':'+min + ':'+new_sec
            elif int(hour)< 10 and int(hour)>0:
                n_hour = int(hour)
                new_time = '0'+str(n_hour) +':'+min + ':'+new_sec
            print new_time
            return new_time
        else:
            print "WORNG CHOICE.. Time format is not proper.."
            return None
    except Exception as e:
        print " Exception generated due to :::",e
        return None


if __name__ == '__main__':
    s = raw_input()

    result = timeConversion(s)
    print result
'''

# Grading Student
# If the difference between the grade and the next higher multiple of 5 is less than 3, round to the next higher multiple of 5
# pass mark is 40, if grade is less than 38 , then nothing to do, becasue it's in FAILING catagory
'''
grades = [76,67,38,33,89]
final_grades = []
for i in grades:
    if i<38:
        final_grades.append(i)
    else:
        j = i%5
        if j>2:
            final_grades.append(i+(5-j))
        else:
            final_grades.append(i)
print final_grades
# s = 75%5
# m = 67%5
# n= 38%5
# o = 38/5
# p = 39%5
#
# print s,m,n,o,p
'''

# Kangarooo Problem
'''
def kangaroo(x1, v1, x2, v2):
    one_pos = x1
    one_val = v1
    two_pos = x2
    two_val = v2
    #temp =0
    #temp2 = 0
    i=0
    while i<10000:
        one_pos = one_pos+one_val
        two_pos = two_pos+two_val
        #print one_pos
        #print two_pos
        if one_pos == two_pos:
            #print "YES"
            #print "LANDED in same pos at %s iteration..."%i
            return "Yes"
        else:
            #print "NO"

            i+=1
    return "NO"

result = kangaroo(0,2,4,1)
print(result)
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
#Forming a Magic Square
# n = int(raw_input('Enter the matrix size:: '))
# r=c=n
# M=[]
# for i in range(0,r):
#     L=[]
#     for j in range(0,c):
#         x = int(raw_input("Enter a digit:"))
#         L.append(x)
#     M.append(L)
#
# for row in M:
#     for x in row:
#         print x,
#     print
# print M
'''
temp =0
M = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
magic_num=3*(3**2+1)/2
print magic_num

sum_list = []
sum_list.extend([sum (lines) for lines in M])
print sum_list

for col in range(len(M[0])):
    sum_list.append(sum(row[col] for row in M))

print sum_list


dlResult = 0
for i in range(0,len(M[0])):
    print M[i][i]
    dlResult +=M[i][i]
sum_list.append(dlResult)

drResult = 0
for i in range(len(M[0])-1,-1,-1):
    print M[i][i]
    drResult +=M[i][i]
sum_list.append(drResult)

print sum_list
if len(set(sum_list))>1:
    print "NOT MAGIC SQUARE"
else:
    print "MAGIC SQUARE"
'''

M = [[4, 8, 2], [4, 5, 7], [6, 1, 6]]
magic_num=3*(3**2+1)/2
print magic_num


row_sum = []
col_sum = []
dia_l=[]
dia_r=[]
sum_list=[]
# for lines in M:
#     row_sum.append(sum(lines))
# print row_sum
#
#
# for col in range(len(M[0])):
#     temp=0
#     for row in M:
#         temp+=row[col]
#     col_sum.append(temp)
# print col_sum

# dlResult = 0
# for i in range(len(M[0])):
#     print M[i][i]
#     dlResult +=M[i][i]
# dia_l.append(dlResult)
# print dia_l

drResult = 0
for col in range(len(M[0])-1,-1,-1):
    for row in range(len(M)):
        print M[row][col]
        #drResult +=M[i][i]
dia_r.append(drResult)

print dia_r