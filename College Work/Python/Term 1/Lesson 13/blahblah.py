list1 = ["abc","male"] 
fw = open(f"file.txt", "w")
for item in list1:
    fw.writelines(item.split())
    