class Person(object) :

    #constructor
    def __init__(self, name) :
        self. name = name

    #to get name
    def getName(self) :
        return self.name
    
    #to check if this person is an employee
    def isEmployee(self) :
        return False


#Inherited or Subclass (Not person in bracket)
class Employee(Person) :

    #here we return the true
    def isEmployee(self) :
        return True

#Driver code
emp = Person("Joni") #An object of Person
print(emp.getName(), emp.isEmployee())

emp = Employee("Wawan") #An object of Employee
print(emp.getName(), emp.isEmployee())