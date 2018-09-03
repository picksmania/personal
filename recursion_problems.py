# Write a Python program to calculate the sum of a list of numbers
'''
def sum_of_list(l):
    result = 1
    if len(l) == 0:
        print "List doesnot have any info.."
    elif len(l) == 1:
        return l[0]
    else:
        return l[0] + sum_of_list(l[1:])

l = [1,2,3,4,5,6]
print sum(l)
'''


# Write a Python program to solve the Fibonacci sequence using recursion
'''
def fibo(n):
    if n==1:
        return 1
    elif n ==2:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

print fibo(5)

'''
# Write a Python program to get the sum of a non-negative integer

'''
def sum_integer(n):
    result =1
    if n == 0:
        return 0
    else:
        print n%10, n/10
        return n % 10 + sum_integer(int(n / 10))

print sum_integer(59)

'''
# Write a Python program to calculate the sum of the positive integers of n+(n-2)+(n-4)... (until n-x =< 0).
# Test Data:
# sum_series(6) -> 12
# sum_series(10) -> 30
'''
def sum_series(n):
  if n < 1:
    return 0
  else:
    return n + sum_series(n - 2)
'''

# Write a Python program to calculate the harmonic sum of n-1
# Note: The harmonic sum is the sum of reciprocals of the positive integers.
# Example :
# harmonic series : 1+ 1/2+1/3+1/4...
'''
def harmonic_series(n):
    if n < 2:
        return 1
    else:
        return 1 / n + (harmonic_series(n-1))

print harmonic_series(77)
'''

import turtle
myTurtle = turtle.Turtle()
myWin = turtle.Screen()

def drawSpiral(myTurtle, lineLen):
    if lineLen > 0:
        myTurtle.forward(lineLen)
        myTurtle.right(90)
        drawSpiral(myTurtle,lineLen-5)

drawSpiral(myTurtle,100)
myWin.exitonclick()