# Ceaser Cipher decode/encode program by Kalel Grobler
'''
This progam is unfinished and still has errors, a rotational sequence still needs to be implimented rather than just adding to the ASCII value.
'''

def encode(rot):
    message = input("Input message: ")
    letters = []
    for letter in message:
        letters.append(ord(letter)+rot)
    ascii_encrypted = [chr(x) for x in letters]
    encrypted_message = "".join(ascii_encrypted)
    print(encrypted_message,"\n")

def decode(rot):
    encrypted_message = input("Input encrypted message: ")
    letters = []
    for letter in encrypted_message:
        letters.append(ord(letter)-rot)
    ascii_decrpyted = [chr(x) for x in letters]
    decrypted_message = "".join(ascii_decrpyted)
    print(decrypted_message,"\n")


def main():
    while True:
        choice = input("1. Encode\n2. Decode \n3. Quit\nChoice:")
        if choice == "1":
            try:
                rot = int(input("Enter ROT: "))
                encode(rot)
            except:
                print("Please input a number.")

        elif choice == "2":
            try:
                rot = int(input("Enter ROT: "))
                decode(rot)
            except:
                print("Please input a number.")
        
        else:
            break

if __name__ == "__main__":
    main()