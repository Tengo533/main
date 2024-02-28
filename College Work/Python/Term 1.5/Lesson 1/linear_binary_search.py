list = [32,43,64,12,23]
target = 23
found = False

def linear():
    for item in list:
        if item == target:
            found = True
            return found

found = linear()
if found == True:
    print("Item in list.")
elif found == False:
    print("Item not in list.")