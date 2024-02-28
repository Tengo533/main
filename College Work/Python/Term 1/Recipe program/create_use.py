
# read not finished

def create_recipe():
    recipe_name = input("Recipe name: ")
    try:
        recipe_people = input("Serving ammount: ")
        int(recipe_people)
    except ValueError:
        print("Please use numbers.")
    with open(recipe_name+".txt","w") as fw:
        fw.writelines(recipe_people+"\n\n")
        try:
            ingredients = int(input("Ingredient ammount: "))
        except ValueError:
            print("Please use numbers.")
        for recipe in range(ingredients):
            ing_name = input("Ingredient name: ")
            fw.writelines(ing_name+"\n")
            ing_ammount = input("Ingredient ammout: ")
            fw.writelines(ing_ammount+"\n")
            ing_type = input("Measurment type: ")
            fw.writelines(ing_type+"\n")
            fw.write("\n")

def use_recipe():
    try:
        file_name = input("File name: ")
        file = file_name + ".txt"
        with open(file, "r") as fr:
            print(fr.readline[0])
    except FileNotFoundError:
        print("File not found.")
    except FileExistsError:
        print("File does not exist.")


def run_program():
    while True:
        choice = input("1. Create a recipe\n2. Use a recipe\n3. Exit\nChoice: ")
        if choice == "1":
            create_recipe()
        elif choice == "2":
            use_recipe()
        elif choice == "3":
            exit()
        else:
            print("Please use 1, 2 or 3.")

run_program()