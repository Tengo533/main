def open_a_file():
    try:
        while True:
            file_name = input("File name: ")
            with open(f"Term 2.5\File Handling\files{file_name}","r") as fh:
                print(fh.read())
                return
    except:
        print("ERROR: File not found.")




def menu():
    try:
        while True:
            choice = int(input("######### MENU #########\n1. Open a file\n2. Write a new file\nChoice: "))
            if choice == 1:
                while True:
                 open_a_file()
                break
            elif choice == 2:
                while True:
                    write_a_file()
                break
            else:
                print("Please input a valid option.")
    except:
        print("ERROR: Please enter a number.")
        

def main():
    menu()


if __name__ == "__main__":
    main()