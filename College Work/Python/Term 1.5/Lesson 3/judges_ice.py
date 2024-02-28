judges = 6
x = 0
lowest = 11
highest = 0
total = 0

for loop in range(0,judges):
    mark = int(input("Mark: "))
    if mark > highest:
        highest = mark
    if mark < lowest:
        lowest = mark
    total = total + mark

result = (total - highest - lowest)
print(f"Highest = {highest} \nLowest = {lowest}")
print("Result = ",result)