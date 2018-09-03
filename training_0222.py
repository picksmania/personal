'''
print "hello"
l = [10,20,30]
try:
    import prasit
    x = int(raw_input("Enter 1st Number::"))
    y = int(raw_input("Enter 1st Number::"))
    s =x/y
    print s
    print l[0]

except ValueError:
    print "GOT Value Error..."
except ZeroDivisionError:
    print "GOT ZeroDivError..."
except IndexError:
    print "GOT Index Error..."
except Exception as e:
    print "Got SOME OTHER Exception...."
    print e
else:
    print "NO EXCEPTION generated...."
finally:
    print "Am in Finally... I do execute all the time..."
print "Rest of the APPS go from here....."
'''
# ==========================================================================
# CLOSURE:
'''
def outer():
    state =10
    def inner():
        return state
    return inner

inn = outer()
r = inn()
print r
'''

#================================================================================
# DECORATORS:
'''
def add10(f):
    def decor(*args):
        return f(*args)+10
    return decor

@add10
@add10
def add(a,b):
    return a+b

s =add(2,3)
print "SUM is::",s
print add.__name__
'''

# paramiterized decorators:
'''
def addn(n):
    def decor(f):
        def reality(*args):
            return f(*args)+n
        return reality
    return decor

@addn(70)
@addn(40)
def add(a,b):
    return a+b

s =add(2,3)
print "SUM is::",s
print add.__name__
'''
#========================================================
# PCIKLE:
'''
import pickle
l = [10,20,[30,40],'hello',{1:2,3:4},60,70]
fout = open('C:\Prasit\serealized.dat','w')
pickle.dump(l,fout)
fout.close()

fin = open('C:\Prasit\serealized.dat','r')
L = pickle.load(fin)
fin.close()
print L
'''
# ===============================================================================
'''
import sys
import os

if len(sys.argv)!= 2:
    print "Application need ONE integer input from CLI..."
    sys.exit(1)

child1 = os.fork()
if child1 == 0:
    print "CHILD_1 started PID::",os.getpid()
    os.execvp('python',['python','fillmatrix.py',sys.argv[1]])

child2 = os.fork()
if child2 == 0:
    print "CHILD_2 started PID::",os.getpid()
    os.execvp('python',['python','fillmatrix.py',sys.argv[1]])

child3 = os.fork()
if child3 == 0:
    print "CHILD_3 started PID::",os.getpid()
    os.execvp('python',['python','fillmatrix.py',sys.argv[1]])

r=1
while True:
    try:
        pid = os.wait()
        print "Process",pid[0],"comleted",r
    except OSError:
        print "****** GAME is OVER *****"
        os.exit(0)
    r=r+1
'''
# ========================================================================
'''
import os

curr_dir = os.getcwd()
listdir = os.listdir(curr_dir)
d ={}

cache_file_name={}

for i in listdir:
    if i.endswith(('py','pyc')):
        cache_file_name[i]={}

print cache_file_name

user_file_name = raw_input("Enter the file name::")
if cache_file_name.has_key(user_file_name):
    print "YOUR FILE IS PRESENT..."

    file_path = os.path.join(curr_dir,user_file_name)
    print file_path
    FR = open(file_path,'r')
    read_file = FR.read()
    read_lines = read_file.split('\n')

    if_count =0
    for_count =0
    for i in read_lines:
        if i.__contains__('if'):
            if_count+=1
        if i.__contains__('for'):
            for_count+=1

    print "Number of IF Loop is:",if_count
    print "Number of FOR loop is",for_count

    print "**************************************************"
    cache_file_name[user_file_name]['if']=if_count
    cache_file_name[user_file_name]['for']=for_count
else:
    print "YOUR FILE IS NOT PRESENT...Select another file.."
print cache_file_name

'''
# =============================================================================


def depth(d, level=1):
    if not isinstance(d, dict) or not d:
        return level
    return max(depth(d[k], level + 1) for k in d)

d ={'a':{'aa':{'aaa':{'aaaa':{}}}}}

c = depth(d,level=1)
print c




























