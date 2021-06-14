# MRO - method resolution order
class A:
    num = 10


class B(A):
    pass


class C(A):
    num = 1


class D(B, C):
    pass


#print(D.mro()) # evaluates attributes and methods based on this order ORDER FIRST -> LAST
print(D.__mro__)
print(D.num)
print(D.__str__) # goes all the way to the object class till it finds the method or attribute


