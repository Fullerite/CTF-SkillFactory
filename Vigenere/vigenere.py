import string

cipher_text = open("output.txt", "r").read()
key = "mysecurekey"  # The key is given

alphabet_lowercase = string.ascii_lowercase
alphabet_uppercase = string.ascii_uppercase
plaint_text = ""  # Flag starts with "Skill"
letters_counter = 0
for i in range(len(cipher_text)):
    if cipher_text[i] in alphabet_lowercase:
        shifted_char = alphabet_lowercase[(alphabet_lowercase.index(cipher_text[i]) - alphabet_lowercase.index(key[letters_counter % len(key)])) % len(alphabet_lowercase)]
        plaint_text += shifted_char
        letters_counter += 1
    elif cipher_text[i] in alphabet_uppercase:
        shifted_char = alphabet_uppercase[(alphabet_uppercase.index(cipher_text[i]) - alphabet_lowercase.index(key[letters_counter % len(key)])) % len(alphabet_uppercase)]
        plaint_text += shifted_char
        letters_counter += 1
    else:
        plaint_text += cipher_text[i]
print(plaint_text)
