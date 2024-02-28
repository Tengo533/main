def times_table():
    table = 0
    x = 0
    while table != 10:
        table += 1
        for x in range(11):
            value = table * x
            print(f"{table} x {x} = {value}")
            x+=1
        print("\n")


def types_of_lists():
    list1 = [1, 2, 3, 4, 5]
    list2 = ["Sam", 2, 10, "hello", 5]
    print(f"Class ID: {list1[0]}, Student Name: {list2[0]}")

my_list = [0,1,2,3,4,5,6,7,8,9]
print( my_list[-2::-2] )