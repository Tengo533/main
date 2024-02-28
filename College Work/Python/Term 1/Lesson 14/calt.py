IngredientsInput = 0
IngredientsRequired = 0
namesstuff = [] # names of ingredients
amountsstuff = [] # number of ingredient
measurementsstuff = [] # measurement of ingredient

choice = input("Do you wish to create or use a recipe? C/U " ).upper()
if choice == "C":
    recipe = input("Enter the name of your recipe: ")
    myfile = open(recipe + ".txt", "w")
    people = (input("Enter the number of people the recipe is for: "))
    myfile.close()
    IngredientsRequired = int(input("How many ingredients are you using? "))
    while IngredientsRequired > IngredientsInput:
        ingredient = input("Enter the name of the ingredient: ")
        amount = (input("Enter the amount required: "))
        measurement = input("Enter the measurement of the ingredient: ")
        namesstuff.append(ingredient)
        amountsstuff.append(amount)
        measurementsstuff.append(measurement)
        IngredientsInput = IngredientsInput + 1
    myfile = open(recipe + ".txt", "a")
    #broken below
    myfile.writelines(people)
    myfile.write("\n")
    myfile.writelines(namesstuff)
    myfile.write("\n")
    myfile.writelines(amountsstuff)
    myfile.write("\n")
    myfile.writelines(measurementsstuff)
    myfile.close()
    print("Complete")
elif choice == "U":
    recipe = input("Enter the name of the recipe you wish to use: ")
    people = input("Enter the number of people the recipe is being used for: ")
    myfile = open(recipe + ".txt", "r")
    myfile.readline(2)
    numbers = [myfile.readline()]
    print(numbers)