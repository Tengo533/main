def example_noncomp():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = []

    for x in fruits:
        if "a" in x:
            newlist.append(x)

    print(newlist)

def example_comp():
    fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
    newlist = [x for x in fruits if x == "apple" ]
    print(newlist)
def hascap(x):
    for letter in x:
        if letter.isupper() == True:
            return True
    return False

myList = ["max","windoW","OS", "greenDee"]

capList = [x for x in myList if hascap(x)==True] # Same as writing loop below                             

#for x in myList:  
#    if hascap(x) == True:
#        capList.append(x)


print(capList)

