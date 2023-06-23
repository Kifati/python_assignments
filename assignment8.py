class A:
    __a=None
    _b=None
    c=None
    def __init__(self,a,b,c): 
        self.__a=a
        self._b=b
        self.c=c
    def display(self):
        print("***Class A***")
        print("The value of a is:",self.__a)
        print("The value of b is:",self._b)
        print("The value of b is:",self.c)
class B(A):
    def display(self):
        try:
            print("***Class B***")
            print("The value of a is:",self.__a)#as a is private data member, it is not inherited by derived class.
        except AttributeError: #exception handled
            print("Can't access private member a")
        print("The value of b is:",self._b)
        print("The value of c is:",self.c)
a1=A(10,20,30)
a1.display()
b1=B(1,2,3)
b1.display()