def binary_search(data, elem):

    low = 0
    high = len(data) -1

    while low <= high:

        middle = (low + high) // 2

        if data[middle] == elem:
            return middle
        elif data[middle] > elem:
            high = middle - 1
        else:
            low = middle + 1

    return -1


mylist=[1,8,10,19,55,63,70]
target=55
posn=binary_search(mylist,target)
print (posn)