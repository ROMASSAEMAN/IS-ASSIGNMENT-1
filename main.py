def caesar_encrypt(text, shift):
    result = ""
    # We loop through every single character in your message
    for char in text:
        # 1. Handle Uppercase letters (A-Z)
        if char.isupper():
            # ord(char) gets the ASCII number (A=65).
            # We subtract 65 to start at 0, add the shift,
            # use % 26 to wrap Z back to A, then add 65 back.
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # 2. Handle Lowercase letters (a-z)
        elif char.islower():
            # Same logic, but using 97 (the ASCII start for 'a')
            result += chr((ord(char) + shift - 97) % 26 + 97)
        # 3. Handle spaces, numbers, and symbols (like @ or !)
        else:
            # These characters are not shifted
            result += char
    return result
def caesar_decrypt(ciphertext, shift):
    # Decrypting is simply reversing the shift (moving backwards)
    return caesar_encrypt(ciphertext, -shift)
# --- Execution  of the message ---
# Your specific input message
message = "Lets go to Islamadad for the project of Ideology @2026"
shift_value = 4  # This means 'a' becomes 'e', 'b' becomes 'f', etc.
# Run the encryption
encrypted = caesar_encrypt(message, shift_value)
# Run the decryption to prove it works
decrypted = caesar_decrypt(encrypted, shift_value)
# Print the results
print(f"Original:  {message}")
print(f"Encrypted: {encrypted}")
print(f"Decrypted: {decrypted}")