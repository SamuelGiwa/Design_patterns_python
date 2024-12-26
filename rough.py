# A Python program to demonstrate inheritance

class Person:

    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id

    # To check if this person is an employee
    def Display(self):
        print(self.name, self.id)


class Emp(Person):
    
    def __new__(cls,x,y):
        # Call the parent class's __new__ method to create an instance
        instance = super(Emp, cls).__new__(cls)
        super(Emp,cls).__init__(x, y)
        return instance

    
    def Print(self):
        print("Emp class called")


# Create an Emp instance
Emp_details = Emp("Mayank", 103)

# Access attributes
print(Emp_details.name_, Emp_details.name)
