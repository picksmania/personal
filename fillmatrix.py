# write a script to compute TIME it takes to fill a square matrix of order N randonly with random Values in the range 1 to 1000 with CLI interface

from datetime import datetime
import random
import sys,os

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
            value = random.randrange(1,30)
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

fh = open(r'C:\Prasit\1.txt','w')
fh.write(str(M))
fh.close()

fr = open(r'C:\Prasit\1.txt','r')
output =fr.readlines()


for i in range(0,len(output)):
    print set(i)
etime = datetime.now()

print "**************************************************"
# print "Time TAKEN to create Default Matrix is %s"%(etime-stime)

os._exit(0)

