fw = open("pin.txt","w")
fr = open("pin.txt","r")
write = input("Input into file: ")
fw.write(write)
fw.close
fr
confirm_written = fr.read()
print(confirm_written)

