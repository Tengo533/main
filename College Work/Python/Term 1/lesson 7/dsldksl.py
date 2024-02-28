PI = 3.141
x = 0
while True:
    def get_area(radius):
        area = PI * (radius**2)
        return area


    radi = float(input("Radius: "))
    function_output = get_area(radi)
    print(f"Area = {function_output}")
    while True:
        run_again = input("Run again? (y/n): ")
        if run_again == "y":
            break
        elif run_again == "n":
            x += 1
            break
        else:
            print("Please use y or n.")
    if x == 1:
        break
print("Exiting...")