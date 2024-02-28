def error_exception(): 
    try:
        num1 = int(input("Num 1: "))
        num2 = int(input("Num 2: "))
        value = num1 / num2

    except TypeError:
        print("TypeError - Bad type.")

    except ZeroDivisionError:
        print("ZeroDivisionError - Numbers not divisible by 0.")
        x = 1

    except NameError:
        print("NameError - Value has no Value.")
    if x < 1:
        print(f"{num1} / {num2} = {value}")






colours = ["blue",  "black", "red", "green", "rose", "rouge"]
new_list = []
for colour in colours:
    if colour[0] == "r":
        new_list.append(colour)

print(new_list)

# 2d list example
2D_list = [ ["1"], ["2"], ["3"],
            ["4"], ["5"], ["6"],
            ["7"], ["8"], ["9"], ]
    