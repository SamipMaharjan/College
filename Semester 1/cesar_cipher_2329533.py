#Welcome message
def welcome():
    print("Welcome to the Caesar Cipher"
    "\nThis program encrypts and decrypts text with the Caesar Cipher.")

#Input taking
def enter_message():
    while True:
        operation = input("Enter if you want to encrypt (e) or decrypt (d) a message:")
        if operation == 'e' or operation == 'd':
            break

        else:
            print("Invalid Mode")

    message = input("Enter what message you would like to encrypt: ")

    while True:
        try:
            global key
            key = int(input("Enter the key (1-25):: "))
            break
        except ValueError:
            print("Invalid Key")
    message = str.upper(message)
    return operation,message

#Encryption
def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            shift = ord(char) + key
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                elif shift < ord('A'):
                    shift += 26
                ciphertext += chr(shift)
            else:
                if shift > ord('z'):
                    shift -= 26
                elif shift < ord('a'):
                    shift += 26
                ciphertext += chr(shift)
        else:
            ciphertext += char
    return ciphertext

#Decryption
def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            shift = ord(char) - key
            if char.isupper():
                if shift > ord('Z'):
                    shift -= 26
                elif shift < ord('A'):
                    shift += 26
                plaintext += chr(shift)
            else:
                if shift > ord('z'):
                    shift -= 26
                elif shift < ord('a'):
                    shift += 26
                plaintext += chr(shift)
        else:
            plaintext += char
    return plaintext

#Main function
def main():
    while True:
        welcome()
        operation,message = enter_message()

        #If the user desires to encrypt.
        if operation.lower() == "e":
            result = encrypt(message, key)
            print("Encrypted message: ", result)

        #If the user desires to decrypt.
        elif operation.lower() == "d":
            result = decrypt(message, key)
            print("Decrypted message: ", result)

        else:
            print("Invalid operation")
        
        while True:
            answer = input("Would you like to encrypt or decrypt another message? (y/n)")
            if answer.lower() == 'y':
                break
            elif answer.lower() == 'n':
                print("")
                return
            else:
                print("Invalid input, please enter 'y' or 'n'")

if __name__ == "__main__":
    main()