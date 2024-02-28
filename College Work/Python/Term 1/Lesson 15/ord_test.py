string = input("input string: ")
key = 2
list = ""
for char in string:
    if char.isalpha():
        is_upper = char.isupper()

        get_position_in_alpha = ord(char) - ord('A' if is_upper else 'a')
        encrypted_char_value = (get_position_in_alpha + key) % 26
        new_character = chr(encrypted_char_value + ord('A'if is_upper else 'a'))
        list += new_character
    else:
        list += char
print(list)