import random
import time

def bubble_sort(ipList):
    listLen = len(ipList) -1
    for count in range(0, listLen):
        swap = False
        for item in range(0, listLen - count):
            if ipList[item] > ipList[item + 1]:
                temp = ipList[item + 1]
                ipList[item + 1] = ipList[item]
                ipList[item] = temp
                swap = True
            
        if swap == False:
            return ipList

def get_random(items, numRange):
    rand_list = []
    for items in range(0, items):
        rint = random.randint(0, numRange)
        rand_list.append(rint)
    return rand_list

def get_time(ipList):
    startTime = time.perf_counter()
    sorted = bubble_sort(ipList)
    endTime = time.perf_counter()
    totalTime = endTime - startTime
    totalTime = round(totalTime, 3)
    return totalTime, sorted

def start():
    while True:
        listLen = input("Length: ")
        numRange = input("Range: ")
        if listLen.isalpha() == True or numRange.isalpha() == True:
            print("Please input numbers.")
        else:
            break

    ipList = get_random(int(listLen), int(numRange))
    sortedList = get_time(ipList)
    print(f"Sorted List: {sortedList[1]}\nTime Taken: {sortedList[0]}s")
start()



