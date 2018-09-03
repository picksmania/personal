"""
This module contains following services..
a. Data: version,L
b. Functions: sample
c. Class : Rectangle, Person, Employee
"""

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















