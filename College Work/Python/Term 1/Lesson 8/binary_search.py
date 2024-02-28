numList = [1,2,3,4,5,6,7,8,9,10]
correctNum = 9

def binary_search():
    while True:
        middle = int(len(numList)) / 2
        if correctNum == middle:
            print(f"Correct number is {middle}")
        low = middle - 1
        high = middle + 1
        if correctNum > low:
            x = low
            while x != 0:
                numList.remove(numList[x])
                x-1
        elif correctNum < high:
            x = high
            while x != len(numList):
                numList.remove(numList[x])
                x+1
binary_search()
            