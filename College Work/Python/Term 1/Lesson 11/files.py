my_file = r"C:\Users\sarah\OneDrive - eastsussexcollegegroup\Python\Lesson 11\text_files\files_test.txt"
count = 0
error = 0
with open(my_file, "r") as fr:
    for lines in fr:
        words = lines.split()
        count += len(words)
        if "ERROR" in words:
            error += 1

print(f"word count = {count}")
print(f"ERROR count = {error}")