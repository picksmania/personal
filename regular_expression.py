import re

# compile() creates regular expression character class [a-e],
# which is equivalent to [abcde].
# class [abcde] will match with string with 'a', 'b', 'c', 'd', 'e'.


# q = re.compile('[a-e]')
# r = re.compile('\d')
# r1 = re.compile('\d+')
# s = re.compile('\D')
# t = re.compile('\s')
# u = re.compile('\S')
# v = re.compile('\w')
# w = re.compile('\W+')

# print(q.findall("I went to him at 11 A.M. on 4th July 1886.He is a #@$%***"))
# print(r.findall("I went to him at 11 A.M. on 4th July 1886.He is a #@$%***"))
# print(r1.findall("I went to him at 11 A.M. on 4th July 1886. He is a #@$%***"))
# print(s.findall("I went to him at 11 A.M. on 4th July 1886.He is a #@$%***"))
# print(t.findall("I went to him at 11 A.M. on 4th July 1886.He is a #@$%***"))
# print(u.findall("I went to him at 11 A.M. on 4th July 1886.He is a #@$%***"))
# print(v.findall("I went to him at 11 A.M. on 4th July 1886.He is a #@$%***"))
# print(w.findall("I went to him at 11 A.M. on 4th July 1886.He is a #@$%***"))
# print type(q), type(r)

# print re.split('[a-f]\d+','Hi HE10llo, hurry come here Watson. his Bday 11th Jan 2001. I know him from 10th Dec 2010',flags=re.IGNORECASE)

str = r'I am Prasit Bagal. I live in Bangalore @ Myhna heights, A-804 appartment.Gunjur 560087. ' \
      r'Prasit is a good boy. Prasit does not own any car now but he wish to have one good CAR in future. ' \
      r'PRASIT BagaL is married'
'''
# a = re.compile('Prasit(?=Bagal)')
# (?iLmsux word/name) --> finds the word/name with IGNORECASE,MULTILINE,LOCALE DEPENDENT,DOT MATCHES ALL,UNICODE, VERBOSE
print "****** 1 ******"
pat = '(?iLmsux)Bagal'
print re.match(pat,str)
print re.search(pat,str)
print re.findall(pat, str)
#m = re.search(pat,str)
#print m.group(0)
#print m.groups(1)
print '===================================='

# This is called a lookahead assertion.

print "****** 2 ******"
pat1 = 'Prasit (?=Bagal)'
print "MATCH:::", re.match(pat1,str)
print "SEARCH:::", re.search(pat1,str)
print "FINDALL:::", re.findall(pat1, str)
print "FINDITER:::", re.finditer(pat1, str)

m = re.compile(pat1,re.I)
print m
print m.sub('RINKI ', str)
#m = re.search(pat1,str)
#print m.group(0)
#print m.groups(1)
print '===================================='

print "****** 3 ******"
# This is called a positive lookbehind assertion.

pat2 = '(?<=Prasit) Bagal'
print "MATCH:::",re.match(pat2, str)
print "SEARCH:::",re.search(pat2, str)
print "FINDALL:::",re.findall(pat2, str)
prasit_iter = re.finditer(pat2, str)
print "FINDITER:::", prasit_iter

m = re.compile(pat2, re.I)
print m
print m.sub(' RINKI',str)
for i in prasit_iter:
      print "starting position:::", i.start()
      print "ending position:::", i.end()
      print "GROUP:::", i.group()

print '===================================='

print "****** 4 ******"

pat3 = 'it?'
print "MATCH:::",re.match(pat3, str)
print "SEARCH:::",re.search(pat3, str)
print "FINDALL:::",re.findall(pat3, str)
print "FINDITER:::",re.finditer(pat3, str)


print '===================================='

print "****** 5 ******"

pat4 = '(?P<Prasit>) Bagal'
print re.match(pat4, str)
print re.search(pat4, str)
print re.findall(pat4, str)
print re.finditer(pat4, str)

print '===================================='

print "****** 6 ******"

str1= r'I am Prasit Bagal. I live in Bangalore @#! Myhna heights, A-804 apartment, Gunjur @#!560087.' \
      r'Prasit is a good boy. Prasit does not own any car now but he wish to have one good CAR in future' \
      r'PRASIT BagaL native is Kolkata'

pat5 = r'([\w-]+\d)'
pat6 = r'([\w-]+) apartment'
print re.match(pat5, str1)
print re.search(pat5, str1)
print re.findall(pat5, str1)
print re.findall(pat6, str1)
'''

str1 ='Bangalore: 560087, Bangalore:560089,Bangalore:560090,Bangalore:560088 ,' \
     'Bangalore:660099,Bangalore:660090,Delhi:560087,Delhi:560088,Delhi:560089,' \
     'bangalore:560078,bangalore:560098'


pat1 = r'\b((?:b|B)angalore):(?=(5(?:\d+)))\b'
c = re.findall(pat1,str1)
#print c

str2 = "Hello my Number is +91-1234567889 and my friend's number is +91-9876543212" \
       "my uncle Number is 080-44441234 and my aunt mumber is +1-1234598765 " \
       "my wife number is +92-8197601520 "
pat2 =r'(\W9[1-3])-(?=(\d{10}))'
d = re.findall(pat2,str2)
#print d

str3 = 'hi hello 832-472-0660 how are you 8197601520 am fine 4444-778700' \
       'done done 281-222-3212 good bad cool woollo 916-332-1110 great man 1234567891' \
       'hhime can dan man'
pat3 = r'\b(([a-zA-z]{2})+)\b'

e = re.findall(pat3,str3)
#print e

str4 = 'Hello shubhamg199630@gmail.com , Rohitneeraj@gmail.com ,' \
        '123prasit@yahoo.com abc 123 dey.rinki_123@hotmail.com'
pat4 = r'\S+@\S+'
f = re.findall(pat4,str4)
#print f

# password must meet four conditions:
#
# 1. The password must have between six and ten word characters \w
# 2. It must include at least one lowercase character [a-z]
# 3. It must include at least three uppercase characters [A-Z]
# 4. It must include at least one digit \d

str5 = 'hi hello Iam23FiNe 832-472-0660 how are you 8197601520. LkEWood1 am fine 4444-778700' \
       'done done 281-222-3212 good bad cool PRASIT woollo 916-332-1110 KAYAL great man 1234567891' \
       'ABCe1 can dan#!~54S?> man rhtdM_@123 and ABC123ac'

# The password length must be greater than or equal to 8
# The password must contain one or more uppercase characters
# The password must contain one or more lowercase characters
# The password must contain one or more numeric values
# The password must contain one or more special characters


#pat5 = r'([(a-zA-z0-9\S)]{6,})'
#pat5 = r'[^a-z]*[a-z]'
#pat5 = r'\A(?=[^a-z]*[a-z])(?=(?:[^A-Z]*[A-Z]){3})(?=\D*\d)\w{6,10}\z'
#pat5 = r'\A(?=\w{6,10}\z)(?=[^a-z]*[a-z])(?=(?:[^A-Z]*[A-Z]){3})\D*\d.*\z'
#pat5 = r'([A-Z]{3,})'
#pat5 = r'([a-z]{1,})'
#pat5 = r'(?=^.{6,}$)(?=.*\d)(?=.*[!@#$%^&*]+)(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$'
pat5 = r'((?=.*\d{1,})(?=.*[a-z]{1,})(?=.*[A-Z]{3,})(?=.*[@#$%]).{6})'
pat6 = r'^(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*[\W]).*'

pwd = re.findall(pat6,str5)
print pwd

'''
fh = open(r'C:\Component_logs\TEMP\nvme.txt','r')
data = fh.read()
#print type(data)
#print data
pat = r'NVMe \S+'
c = re.findall(pat,data)
print list(set(c))
'''

# Fetchng the FILE NAME from a FILE PATH

'''
str5 = r'C:\test_project\SKP_MH_Project\regular_expression.py ' \
       r'C:\test_project\SKP_MH_Project\regular.log'

pat2 = r'((?:[^\\]*).(?:py|log))'
print str5
#s = re.findall(pat,str5)
m = re.findall(pat2,str5,re.M)
#print s
print m
'''