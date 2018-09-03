import re
'''
# Write a script to count numbers of words available in a given string
pra = 'Prasit is a boy. He lives in Bangalore. He is from Kolkata'
d ={}
pra_list = pra.split(' ')
#print pra_list
for x in pra_list:
    print x,pra_list.count(x)

# Write a script to count number of words which begins with Upper case alphabet
    if x[0].isupper():
        print x,pra_list.count(x)

# Write a script to swap FIRST and LAST character of every word of a given string.
    tmp = x[1:-1]
    print tmp
    print x[-1:]+ tmp+ x[:1]

# Write a script to remove duplicate words available in a given string.
#print set(pra_list)

# Write a script to find frequency occurrence of words of a given string
    if x in d.keys():
        d[x]+=1
    else:
        d[x]=1

print d
'''


mat1 = []
mat2 = []

x = [1,2,3]
y= [4,5,6]
w = [7,8,9]
z = [4,6,8]
mat1.append(x)
mat1.append(y)
mat2.append(w)
mat2.append(z)
print mat1,mat2

result = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(mat1)):
    for j in range(len(mat1[0])):
        print mat1[i][j]
        print mat2[i][j]
        result[i][j]=mat1[i][j]+mat2[i][j]

for r in result:
    print r


'''
# write a script  to find smallest integer out of 3 integer.
x =[10,34,54,23,56]
print min(x),type(x[0])
'''