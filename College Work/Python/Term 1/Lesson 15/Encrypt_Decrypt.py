def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            is_upper = char.isupper()

            get_position_in_alpha = ord(char) - ord('A' if is_upper else 'a')
            encrypted_char_value = (get_position_in_alpha + shift) % 26
            new_character = chr(encrypted_char_value + ord('A'if is_upper else 'a'))
            result += new_character
        else:
            result += char
    return result

def decrypt(text, shift):
    shift = -shift
    encrypt(text,shift)

def start():
    while True:
        choice = input("\n\nWould you like to:\n1. Encrypt\n2. Decrypt\n3. Exit\nChoice: ")
        if choice == "1":
            text = input("\nInput original text: ")
            shift = int(input("\nInput shift ammount: "))
            result = encrypt(text,shift)
            print(f"Encrypted text: {result}")
        elif choice =="2":
            text = input("\nInput original text: ")
            shift = int(input("\nInput shift ammount: "))
            result = decrypt(text,shift)
            print(f"Decrypted text: {result}")
        elif choice =="3":
            break
        else:
            print("Please use 1, 2 or 3.")

start()