class Student:
    school="AkiraChix"
    def __init__(self,first_name, last_name, age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age

    def speak(self):
        return f"Hello class my name is {self.name}"
    def year_of_birth(self):
        return f"Hello {self.name} I was born in {2021-self.age}"
    def greet(self):
        return f"Hello{self.first_name}welcome to {self.school}"
    
    