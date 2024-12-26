class Person:
    def __init__(self,name,age,university,degree):
        self.name = name.title()
        self.age = age
        self.university = university.title()
        self.degree = degree
        
    @classmethod
    def from_csv_line(cls,line:str) -> "Person":
        return cls(*line.strip().split(","))
    
with open("people.csv","r") as file:
    lines = file.readlines()
    
lines = [line.strip() for line in lines[0:]]

person_list = [Person(*line.split(",")) for line in lines]

for person in person_list:
    print(
        f"{person.name} is {person.age}, studying {person.degree} at {person.university}."
    )        
    
    