def version1():
    myList = [11,32,2,75,8,92]

    listMax = max(myList)
    listMin = min(myList)

    result = listMax - listMin

    print(result)

def version2():
    myList = [11,32,2,75,8,92]

    def findMax():
        newMax = 0
        for item in myList:
            if item > newMax:
                newMax = item
        return newMax
    
    def findMin():
        newMin = 0
        for item in myList:
            if item < newMin:
                newMin = item
        return newMin
    
    listMax = findMax()
    listMin = findMin()
    result = listMax - listMin
    print(result)

version2()