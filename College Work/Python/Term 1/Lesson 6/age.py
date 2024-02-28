def age():
    while True:
        age = int(input("Enter age: "))

        if age > 150 or age < 1:
            print("Invalid age, must be lower than 150 and higher than 0.")
        else:
            print("Age accepted.")
            break

    print(f"You are {age} years old.")

def triangle():
    a = int(input("Side A: "))
    b = int(input("Side B: "))
    c = int(input("Side C: "))
    if a < 1 or b < 1 or c < 1:
        print("You must input a vaild length.")
    
    if a != b and b != c and a != c:
        print("Scalene.")
    elif a == b and b == c:
        print("Equilateral.")
    else:
        print("Isosceles.")

def traffic_light():
    my_var = "red"
    if my_var == "red":
        print("STOP")
    elif my_var == "orange":
        print("STOP IF POSSIBLE")
    elif my_var == "green":
        print("GO")
    else:
        print("NEGOTIATE WITH CAUTION")

def student_score():
    student_score = 40
    if student_score <= 40:
        print("D")
    elif student_score <= 60:
        print("C")
    elif student_score <= 80:
        print("B")
    else:
        print("A")
student_score()