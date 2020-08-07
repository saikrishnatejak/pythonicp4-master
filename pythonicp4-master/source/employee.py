class Employee:   #Create a class
    no_of_employees=0#intialize the number of employees
    sum=0
    avgsal=0
    def __init__(self,name,family,salary,department):#constructor ,we have some variables
        self.name=name
        self.family=family
        self.salary=salary
        self.department=department
        Employee.no_of_employees+=1
        Employee.sum+=self.salary
    def avg_salary(self):
        Employee.avgsal=Employee.sum/Employee.no_of_employees#Here we find the Average
        print('average is',Employee.avgsal)
    def Details(self):
        print("name","family","salary","department",self.name,self.family,self.salary,self.department)
class Fulltime_employee(Employee):# here we have inherited the values from Employee class
    def __init__(self,name,family,salary,department):#This is a second constructor
      Employee.__init__(self,name,family,salary,department)

employee1=Fulltime_employee("Madhukar","vuradi",10000,"cs")#Created instances of 2 super class
employee2=Fulltime_employee("Ram","Guduri",50000,"cs")# Created instances of 2 sub class
employee1.Details()# Here we print the details
employee2.Details()
employee1.avg_salary()
