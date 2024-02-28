#----------------------------------------------------------
# Insertion Sort in ascending order
# By Brian Maskell - 9/11/2020
# Classic algo - could optimise by just inserting at end
#----------------------------------------------------------


#---
# InsertionSort Function
def insertion_sort(ip_list):
    list_len = len(ip_list)

    for index in range(1, list_len):     # nb: range excludes last num (lists use 0 index)
        current_entry = ip_list[index]   # get next entry to insert in correct location
        print("-> Processing entry " + str(current_entry))

        pos = index                      # temp variable to keep track of start point for this iteration

        # Shuffle entries up while current entries value is less than position in list we are checking 
        while pos > 0 and ip_list[pos-1] > current_entry:
            print("Swapping {} for {}".format(ip_list[pos], ip_list[pos-1]))
            temp = my_list[pos]
            my_list[pos] = my_list[pos-1]
            my_list[pos-1] = temp
            print(temp)

            print("Shuffled List: " + str(ip_list))         # print list after shuffle
             
            pos -= 1                     # decrement pos variable

    # NB: List sorted in place hence no need to return a new lists


#---
# Test sort function
def test_sort(ip_list, ref_list):
    
    if ip_list == ref_list:
        print("Test Passed!")
    else:
        print("Test Failed.")


#===
# MAIN PROGRAM
#===

my_list = [16, 92, 84 , 68]            # create list

print("STARTING, Sorting list: " + str(my_list))

insertion_sort(my_list)              # call sort function - list is sorted in-place

print("FINISHED, Sorted list: " + str(my_list))
ref_list = [16, 68, 84, 92]

test_sort(my_list, ref_list)



