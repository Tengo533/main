habitats = ["Desert", "Rainforest", "Jungle", "Plains", "Mesa"]

class Turtle:
    def __init__(self, name, age, size, colour, habitat):
        self.name = name
        self.age = age
        self.size = size
        self.colour = colour
        self.habitat = habitat
    
    def Poop(Turtle):
        print(f"{Turtle.name} pooped")
    
    def Birthday(Turtle):
        Turtle.age += 1
        print(f"Happy birthday {Turtle.name}, they grew up and are now {Turtle.age} years old!")
    
    def Grow(Turtle):
        if Turtle.habitat in habitats[0]:
            Turtle.size = Turtle.size*1.2
        else:
            Turtle.size = Turtle.size*1.1

my_turtle = Turtle("Goop", 12, 30, "Blue", "Desert")

my_turtle.Grow()
print(my_turtle.size)