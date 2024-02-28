# Object Orientated Programming

class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_age(self, age):
        self.age = age

    def get_age_average(self, age):
        value = 0
        for age in d.get_age:
            value += age

d = Dog("Tim", 34)
d2 = Dog("Tim", 12)
d3 = Dog("Tim", 32)
print()