def caesarCipher(s, k):
    encrypted = ""
    for char in s:
        if char.isalpha():
            char_code = ord(char)
            base_code = 65 if char.isupper() else 97
            shifted_code = (char_code - base_code + k) % 26 + base_code
            encrypted += chr(shifted_code)
        else:
            encrypted += char
    return encrypted
