PI = 3.14 # Constant value
def circle_area(ip_radius):
    area = PI * (ip_radius*ip_radius)
    return area
def circle_circumference(ip_radius): # Takes in the argument ip_radius
    circum = 2 * PI * ip_radius # 2 times the Constant PI, the timesed by the ip_radius
    return circum   # Returns the value given by the calculation
circum = circle_circumference(5) 
area = circle_area(5)
print(f"Circumference: {circum} \nArea: {area}")
