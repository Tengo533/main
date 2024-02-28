psw = input("Input Master Password: ")
master_password = "Password"
if psw == master_password:
    f = open('C:\Users\sarah\OneDrive - eastsussexcollegegroup\Python\Lesson 4\password_manager\passwords.txt', 'r')
    printpass = f.read
    print(printpass)