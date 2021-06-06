# caesar cipher
def encrypt(text, s):
    result = ""

    # traverse text
    for i in range(len(text)):
        char = text[i]

        # Encrypt uppercase characters
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)

    return result


# check the above function
message = str(input(" ENTER THE TEXT TO BE ENCODED WITH CAESER TECHNIQUE: "))
shift = int(input(" ENTER THE SHIFT FOR CAESER TECHNIQUE:"))
print("Text  : " + message)
print("Shift : " + str(shift))
print("Cipher: " + encrypt(message, shift))
