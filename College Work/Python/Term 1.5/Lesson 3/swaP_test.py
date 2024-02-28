
my_list = [2,5,3,6,1]
ent = 1
def swap_5_3():
    print(my_list,"\n")
    #3 lines of code 
    temp = my_list[ent]
    my_list[1],my_list[2] = my_list[2], temp
    #----------------
    print(my_list)

def swap_notemp():
    print(my_list)
    my_list[ent] = my_list[ent] + my_list[ent+1]
    my_list[ent+1] = my_list[ent] - my_list[ent+1]
    my_list[ent] = my_list [ent] - my_list[ent+1]
    print(my_list)
swap_notemp()