#===============================
#===============================
# Merge Sort Algorithm 
# - using recursion
#===============================
#===============================


#---
# Merge function - glue spliced elements back together in sorted order
# lhs = left hand side, rhs = right hand side
# NB: dont believe merge functionality will be in exam
def merge(ip_list, lhs_idx, rhs_idx, mid_idx):
    
    print(" "*4 + "Merge called with lhs=" + str(lhs_idx) + ", rhs=" + str(rhs_idx) 
          + ", mid=" + str(mid_idx) + ", list=" + str(ip_list[lhs_idx:rhs_idx+1]))

    # Create 2 lists representing the sub-lists we want to merge
    rhs_copy  = ip_list[lhs_idx:mid_idx+1]
    lhs_copy = ip_list[mid_idx+1:rhs_idx+1]  # nb: +1 for 2nd arg as non-inclusive

    # Index variables to track where we are looping through each list 
    lhs_copy_idx = 0
    rhs_copy_idx = 0
    sorted_idx = lhs_idx

    # Loop while we elements in either low list or high list to process
    while lhs_copy_idx < len(lhs_copy) and rhs_copy_idx < len(rhs_copy):
    
        # If current element in low list is smaller than current element in high list
        # then copy the low list element value into the sorted list and increment
        # index as now populated in sorted list
        if lhs_copy[lhs_copy_idx] <= rhs_copy[rhs_copy_idx]:
            ip_list[sorted_idx] = lhs_copy[lhs_copy_idx]
            lhs_copy_idx += 1
        # Otherwise must other way round and rhs list has the lower value to copy
        # over to the sorted list
        else:
            ip_list[sorted_idx] = rhs_copy[rhs_copy_idx]
            rhs_copy_idx += 1

        # Regardless of which list we copied our element from we need to increment
        # the index of the sorted list so can accept the next value
        sorted_idx += 1

    # Get here then we have exhausted one of the lists hence can just copy the remaining
    # elements of the list still containing uncopied elements.

    # Copy any remaining elements in lhs list across to the sorted list
    while lhs_copy_idx < len(lhs_copy):
        ip_list[sorted_idx] = lhs_copy[lhs_copy_idx] 
        # Increment both source and destination indexs
        lhs_copy_idx += 1
        sorted_idx +=1

    # Copy any remaining elements in rhs list across to the sorted list
    while rhs_copy_idx < len(rhs_copy):
        ip_list[sorted_idx] = rhs_copy[rhs_copy_idx] 
        # Increment both source and destination indexs
        rhs_copy_idx += 1
        sorted_idx +=1

    print(" "*6 + "Merge created sorted sub-list=" + str(ip_list[lhs_idx:rhs_idx+1]))



# ---
# sort ip_list using merge sort algorithm
def merge_sort(ip_list, lhs_idx, rhs_idx):

    # nb: for python slices, the start point is inclusive but the end point exclusive hence +1 at end
    print("MergeSort called with lhs=" + str(lhs_idx) + ", rhs=" + str(rhs_idx) 
          + ", list=" + str(ip_list[lhs_idx:rhs_idx+1]))

    # Check if reached exit condition where list fully split
    if lhs_idx >= rhs_idx:
        return

    # Find mid-point between left and right indexs
    mid_idx = (lhs_idx + rhs_idx) // 2     # integer floor division

    #Call myself using new values representing the list split in 2
    merge_sort(ip_list, lhs_idx, mid_idx)     # rhs branch 
    merge_sort(ip_list, mid_idx+1, rhs_idx)   # lhs branch

    # Get here then recursive calls are all done
    print(" "*2 + "A Branch Dividing Stage Completed")

    # Merge the split out elements back together in sorted order
    merge(ip_list, lhs_idx, rhs_idx, mid_idx)



#-------------
# Main Code
#-------------

# List to be sorted
my_list = [20, 10, 30, 40, 5, 20]   

# Starting values
ip_len = len(my_list)               # num elements in list
low = 0                             # initial lower boundary
high = ip_len -1                    # initial higher boundary


print("START Unsorted List: " + str(my_list))
merge_sort(my_list, low, high)
print("FINISHED Sorted List: " + str(my_list))




#------------------------------------------------
# FOR REFERENCE ONLY - EXAMPLE PROGRAM OUTPUT
#------------------------------------------------

# nb: """" used to start and end a multiline comment

"""
START Unsorted List: [20, 10, 30, 40, 5, 20]
MergeSort called with lhs=0, rhs=5, list=[20, 10, 30, 40, 5, 20]
MergeSort called with lhs=0, rhs=2, list=[20, 10, 30]
MergeSort called with lhs=0, rhs=1, list=[20, 10]
MergeSort called with lhs=0, rhs=0, list=[20]
MergeSort called with lhs=1, rhs=1, list=[10]
  A Branch Dividing Stage Completed
    Merge called with lhs=0, rhs=1, mid=0, list=[20, 10]
      Merge created sorted sub-list=[10, 20]
MergeSort called with lhs=2, rhs=2, list=[30]
  A Branch Dividing Stage Completed
    Merge called with lhs=0, rhs=2, mid=1, list=[10, 20, 30]
      Merge created sorted sub-list=[10, 20, 30]
MergeSort called with lhs=3, rhs=5, list=[40, 5, 20]
MergeSort called with lhs=3, rhs=4, list=[40, 5]
MergeSort called with lhs=3, rhs=3, list=[40]
MergeSort called with lhs=4, rhs=4, list=[5]
  A Branch Dividing Stage Completed
    Merge called with lhs=3, rhs=4, mid=3, list=[40, 5]
      Merge created sorted sub-list=[5, 40]
MergeSort called with lhs=5, rhs=5, list=[20]
  A Branch Dividing Stage Completed
    Merge called with lhs=3, rhs=5, mid=4, list=[5, 40, 20]
      Merge created sorted sub-list=[5, 20, 40]
  A Branch Dividing Stage Completed
    Merge called with lhs=0, rhs=5, mid=2, list=[10, 20, 30, 5, 20, 
40]
      Merge created sorted sub-list=[5, 10, 20, 20, 30, 40]
FINISHED Sorted List: [5, 10, 20, 20, 30, 40]
"""