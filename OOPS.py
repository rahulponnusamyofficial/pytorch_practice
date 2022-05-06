class Employee:
    def __init__(self, first, last, pay):
       self.first=first
       self.last=last
       self.email=first+'.'+last+'@gmail.com'
       self.pay=pay
    def fullname(self):
        return '{} {}'.format(self.first,self.last)
    
emp1 = Employee("rahul", "ponnusamy", 50000)
emp2 = Employee("prasannakumar", "kumaresan", 60000)

# print(emp1)
# print(emp2)


# emp1.first="rahul"
# emp1.last="ponnusamy"
# emp1.email="rahulponnusamy@gmail.com"
# emp1.pay=50000

# emp2.first="prasanna kumar"
# emp2.last="kumaresan"
# emp2.email="prasannakumarkumaresan@gmail.com"
# emp2.pay=50000

print(emp1.email)
print(emp2.email)
print(emp1.fullname())
print(emp2.fullname())

print(emp2.fullname())
print(Employee.fullname(emp2))