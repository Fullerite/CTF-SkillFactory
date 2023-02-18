import string

cipher_text = open("output.txt", "r").read()

alphabet_lowercase = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase
shift = ord("S") - ord(cipher_text[0])  # Flag starts with "Skill"
plain_text = ''

for char in cipher_text:
    if char in alphabet_lowercase:
        shifted_char = alphabet_lowercase[(alphabet_lowercase.index(char) + shift) % len(alphabet_lowercase)]
        plain_text += shifted_char
    elif char in alphabet_uppercase:
        shifted_char = alphabet_uppercase[(alphabet_uppercase.index(char) + shift) % len(alphabet_uppercase)]
        plain_text += shifted_char
    else:
        plain_text += char

print(plain_text)
