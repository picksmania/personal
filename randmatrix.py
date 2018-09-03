import sys
import os

if len(sys.argv)!= 2:
    print "Application need ONE integer input from CLI..."
    sys.exit(1)

child1 = os.fork()
if child1 == 0:
    print "CHILD_1 started PID::",os.getpid()
    child1_pid = os.getpid()
    os.execvp('python',['python','fillmatrix.py',sys.argv[1]])

child2 = os.fork()
if child2 == 0:
    print "CHILD_2 started PID::",os.getpid()
    child2_pid = os.getpid()
    os.execvp('python',['python','fillmatrix.py',sys.argv[1]])

child3 = os.fork()
if child3 == 0:
    print "CHILD_3 started PID::",os.getpid()
    child3_pid = os.getpid()
    os.execvp('python',['python','fillmatrix.py',sys.argv[1]])

r=1
while True:
    try:
        pid = os.wait()
        print "Process",pid[0],"comleted",r
    except OSError:
        print "****** GAME is OVER *****"
    finally:
        chilld4 = os.fork()
        if chilld4==0:
            print "CHILD_4 started PID::",os.getpid()
            for i in range(3):
                fin = open('/home/prasit/%s.log'%child1_pid,'r')
                output = fin.readlines()
                a = out



        os._exit(0)
    r=r+1
