#parent class
class Person(object) :
    def __init__(self, name, idnumber) :
        self.name = name
        self.idnumber = idnumber
    def display(self) :
        print(self.name)
        print(self.idnumber)

#child class 
class Employee(Person) :
    def __init__(self, name, idnumber, salary, post) :
        self.salary = salary
        self.post = post

        #invoking the __init__ of the parent class
        Person.__init__(self, name, idnumber)


#creation of an object variable or an instance
a = Employee('Rahul', 998870, 3000000, "Intern")

#calling a function of the class Person using its instance
a.display()