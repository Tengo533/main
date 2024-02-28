class Human():
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height
    
    def cm_to_feet(height):
        feet = height / 30.48
        feet = round(feet,2)
        return f"Your height in feet is {feet} foot."


human1 = Human("Kalel",17,160)
print(human1.name,human1.age,human1.height)
print(Human.cm_to_feet(human1.height))
                                                