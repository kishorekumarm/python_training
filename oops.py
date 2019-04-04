# Object Oriented programming in Python

# Basic Class
# Attributes - class attributes and instance Attributes
'''
class Employee:
    name = 'Vinay'

employeeOne = Employee()
print(employeeOne.name)
employeeOne.age = 25
print(employeeOne.age)
employeeTwo = Employee()
employeeTwo.name = 'Nitin'
print(employeeTwo.name)
'''
'''
# Usage of self parameter
class Employee:
    name = 'Vinay'
    def displayEmpName(self):
        print(self.name)

employeeOne = Employee()
employeeOne.displayEmpName()
'''
'''
# Usage of static method
class Employee:
    name = 'Vinay'
    @staticmethod
    def displayString():
        print('Displaying non-class related string')

employeeOne = Employee()
employeeOne.displayString()
'''
'''
# Usage of init method
class Employee:
    def setEmpName(self):
        self.name = 'Vinay'
    def displayEmpName(self):
        print(self.name)

employeeOne = Employee()
employeeOne.displayEmpName()
'''
'''
class Employee:
    def __init__(self):
        self.name = 'Vinay'
    def setEmpName(self):
        self.name = 'Vinay'
    def displayEmpName(self):
        print(self.name)

employeeOne = Employee()
employeeOne.displayEmpName()
'''
'''
class Employee:
    def __init__(self,name):
        self.name = name
    def setEmpName(self):
        self.name = 'Vinay'
    def displayEmpName(self):
        print(self.name)

employeeOne = Employee('Nitin')
employeeOne.displayEmpName()
'''

'''
# Inheritance
# Note that class attributes and clas methods alone can be inherited.
class Employee:
    num_working_hours = 37.5

class dwhTeam(Employee):
    def __init__(self):
        print(self.num_working_hours)

teammember = dwhTeam()
'''

'''
# Encapsulation
# public define attributes just as is - name
# protected define attributes - _name
# private define attributes - __name

class Employee:
    name = 'Vinay'
    _workinghours = 120
    __department = 'Data Engineering' # Name gets saved as _Employee__department

class dwhTeam(Employee):
    def displayInfo(self):
        print("Name of the employee is {0} and he is working for {1} hours".format(self.name,self._workinghours))
        print("Also he belongs to {}".format(self._Employee__department))

teammember = dwhTeam()
teammember.displayInfo()
'''

'''
# Polymorphism
# Operator overloading

class Square:
    def __init__(self,value):
        self.value=value

    def __add__(obj1,obj2):
        print(obj1.value + obj2.value)

squareone = Square(2)
squaretwo = Square(3)
s = squareone + squaretwo
'''

# Polymorphism
# Method overriding
class Employee:
    #workinghours =37.5
    def __init__(self):
        pass
    def setworkingHours(self):
        self.workinghours = 37.5
    def displayWorkingHours(self):
        print(self.workinghours)

class dwhTeam(Employee):
    def setworkingHours(self):
        self.workinghours = 45
        #print(self.workinghours)

    def resetworkingHours(self):
        super().setworkingHours()

teammember = dwhTeam()
teammember.setworkingHours()
teammember.displayWorkingHours()
teammember.resetworkingHours()
teammember.displayWorkingHours()
