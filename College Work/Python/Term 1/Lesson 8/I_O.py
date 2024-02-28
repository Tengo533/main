def tri_area():
    while True:
        triangle_base = int(input("Triange base: "))
        triangle_height = int(input("Triange height: "))

        area = 0.5 * triangle_base * triangle_height

        print(f"Base: {triangle_base}\nHeight: {triangle_height}\nArea: {area}")
        
        while True:
            again = input("Run again? (y/n): ")
            if again == "y":
                break
            if again == "n":
                exit()
            else:
                print("Please use y or n.")

def two_func():
    a = input("Input: ")
    print(a)

def go_success():
    while True:
        x = input("Input: ")
        if x == "GO":
            break
        else:
            continue
    print("SUCCESS")

def vowel_count():
    vowels = ["a","e","i","o","u"]
    count = 0
    user_input = input("Input: ")
    length = len(user_input)
    print(length)
    i = 0
    while i != length:
        if user_input[i] in vowels:
            count = count + 1
            i = i + 1
    print(f"Vowels: {count}")
vowel_count()