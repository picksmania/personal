# class Person:
#     # Define the class parameter "name"
#     name = "Person"
#
#     def __init__(self, name = None):
#         # self.name is the instance parameter
#         self.name = name
#
# jeffrey = Person("Jeffrey")
# print "%s name is %s" % (Person.name, jeffrey.name)
#
# nico = Person()
# nico.name = "Nico"
# print "%s name is %s" % (Person.name, nico.name)
def f(n):
    if n == 0: return 0
    elif n == 1: return 1
    else: return f(n-1)+f(n-2)

n=int(raw_input())

values = [str(f(x)) for x in range(0, n+1)]
print ",".join(values)



