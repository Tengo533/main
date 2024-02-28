def bubbleSorter():    
#This program is designed to take in a randomly generated set of numbers and sort them using the bubble sort method
    import random
    import time

    def bubbleSort(ipList):
        listLen = len(ipList)
        for count in range(0, listLen):
            swap = False
            for item in range(0, listLen -1 -count):
                if ipList[item] > ipList[item + 1]:
                    temp = ipList[item + 1]
                    ipList[item + 1] = ipList[item]
                    ipList[item] = temp
                    swap = True
            
            if swap == False:
                return ipList

    def getRandomList(listLen):
        randomList = []
        for item in range(0, listLen):
            rnd_num = random.randint(0, 100)
            randomList.append(rnd_num)    

        return randomList

    def timeEfficencyTrial():
        testList = [10, 100 , 1000, 10000, 100000]
        for i in testList:
            startTime = time.perf_counter()
            bubbleSort(getRandomList(i))
            endTime = time.perf_counter()
            timeDiff = round(endTime - startTime, 4)
            print(f"Time taken for a list of {i}: {timeDiff} seconds")

    def main():
        while True:
            choice = input("Would you like to sort a random list, or test how long it takes to sort a increase size of lists? (1, 2)")
            if choice == "1":
                listLen = int(input("Input list length: "))
                randomList = getRandomList(listLen)
                print(randomList)
                sortedList = bubbleSort(randomList)
                print(f"Random list sorted: {sortedList}")
            elif choice == "2":
                timeEfficencyTrial()

    main()  