class Car:
    make="Mazda"
    def __init__(self,numberPlate,color):
        self.numberPlate=numberPlate 
        self.color=color

    def hoot(self):
       return f"My car number is {self.numberPlate}" 
    def carry(self):
        return f"My car is {self.color}"


    
