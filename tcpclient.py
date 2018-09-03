import socket
import os,sys

HOST = '127.0.0.1'
PORT = 6000
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))
while True:
    print "     MENU      "
    print "1. testprime   "
    print "2. nextprime   "
    print "3. filedownload   "
    print "4. exit \n"
    ch = raw_input("Please enter your choice....")
    if ch == '4':
        s.sendall(ch)
        print "bye"
        break

    if int(ch) < 1 or int(ch) > 3:
        os.system('clear')
        print "Improper choice... Choose right service.."
        continue

    elif int(ch) == 1 or int(ch)== 2:
        n = raw_input("Enter One number...")
        data = ch + ":" + n
    elif int(ch) == 3:
        n = raw_input("Enter the file name...")
        curr_dir = os.getcwd()
        data = os.path.join(curr_dir,n)

    s.sendall(data)
    result = s.recv(1024)
    os.system("clear")
    if int(ch) == 1 or int(ch)== 2:
        print "result from server:::",result
    elif int(ch) == 3:
        fh = open('\home\prasit\download\%s'%n,'w')
        fh.write(result)
        fh.close()

s.close()