def encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            # Shift the letter by the shift amount
            start = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - start + shift) % 26 + start)
        else:
            result += char
    return result

message = input("Enter a message to encrypt: ")
print("🔒 Ciphertext: " + encrypt(message, 3))    