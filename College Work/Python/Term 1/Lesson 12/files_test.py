x=1

with open(r"C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Lesson 12\text_test.txt","w") as fw:
    while True:
        line = input("Add line: ")
        fw.write(line)
        fw.write("\n")
        choice = input("Stop adding lines?")
        if choice == "y":
            break
        elif choice == "n":
            continue

with open(r"C:\Users\546003\OneDrive - eastsussexcollegegroup\Python\Lesson 12\text_test.txt","r") as fr:
    for lines in fr:
        print(lines)