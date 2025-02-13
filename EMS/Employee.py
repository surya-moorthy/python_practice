

class employee:

    def __init__(self,name,id,age,salary):
        self.name = name
        self.id = id
        self.age = age
        self.salary = salary
    
    def __str__(self):
        return f"{self.name} reached {self.age} age and his salary is {self.salary}"


    