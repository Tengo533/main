def open_a_file():
    try:
        while True:
            file_name = input("File name: ")
            full_path = r"D:\github\main\College Work\Python\Term 2.5\File Handling\files" + f"\{file_name}"
            print(full_path)
            with open(f"{full_path}.txt","r") as fh:
                print("\n",fh.read())
                return
    except:
        print("ERROR: File not found.")

def write_a_file():
    try:
        write_name = input("Document Name: ")
        full_path = r"D:\github\main\College Work\Python\Term 2.5\File Handling\files" + f"\{write_name}"
        with open(f"{full_path}.txt", "w") as fh:
            lines = []
            print("Enter text (type 'done' on a new line to finish):")
            while True:
                line = input()
                if line.strip().lower() == 'done':
                    break
                lines.append(line)
                text = "\n".join(lines)
            fh.write(text)
            return
    except:
        print("ERROR")

def menu():
    try:
        while True:
            choice = int(input("######### MENU #########\n1. Open a file\n2. Write a new file\n3. Quit\nChoice: "))
            if choice == 1:
                open_a_file()

            elif choice == 2:
                write_a_file()

            elif choice == 3:
                break

            else:
                print("Please input a valid option.")
    except:
        print("ERROR: Please enter a number.")
        

def main():
    menu()


if __name__ == "__main__":
    main()