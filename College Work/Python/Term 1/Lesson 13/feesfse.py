PI = 3.141

class Ball:
    
    def __init__(self, radius, colour):
        self.radius = radius # int
        self.colour = colour # str

    def set_radius(radius):
        radius = input("Radius: ")
        radius = int(radius)
        return radius
    
    def get_colour(colour):
        return f"The ball colour is {colour}."
    
    def get_volume(radius):
        volume = (4/3)*PI*(radius**3)
        return f"The volume of the ball is {volume}"
    

        
#set the radius of the ball:  Ball.__setattr__(ball1, "radius", Ball.set_radius(radius=0))

cricket_ball = Ball(10, "Red")

tennis_ball = Ball(8, "Green")

print(cricket_ball.colour)

get_radius = Ball.__setattr__(tennis_ball, "radius", Ball.set_radius(radius=0))
print(f"Volume: {tennis_ball.get_volume()}")


