import json

class Person:
    def __init__(self,name,age,university,degree):
        self.name = name.title()
        self.age = age
        self.university = university.title()
        self.degree = degree
        
    @classmethod
    def from_csv_line(cls,line:str) -> "Person":
        return cls(*line.strip().split(","))
    
    @classmethod
    def from_json(cls, json_str: str) -> "Person":
        """Create a Person object from a JSON string"""
        data = json.loads(json_str)
        return cls(data['name'], data['age'], data['university'], data['degree'])


def read_file_and_create_person(file_path: str):
    # Detect file type based on the extension
    if file_path.endswith('.json'):
        with open(file_path, 'r') as file:
            data = json.load(file)            
            person_list = [Person.from_json(json.dumps(person)) for person in data]
            
    elif file_path.endswith('.csv'):
        with open(file_path, 'r') as file:
            lines = file.readlines()
            person_list = [Person.from_csv_line(line) for line in lines[1:]]  # Assuming header row
            
    else:
        raise ValueError("Unsupported file type. Please provide a .csv or .json file.")
    
    for person in person_list:
        print(f"{person.name} is {person.age}, studying {person.degree} at {person.university}.")



# Example usage for a CSV file
#read_file_and_create_person('people.csv')

# Example usage for a JSON file
read_file_and_create_person('people.json')

    
