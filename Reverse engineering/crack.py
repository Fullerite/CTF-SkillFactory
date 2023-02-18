secret_key = "08 0A 0F 0F 18 14 0C 14 3C 16 3C 11 50 57 0F 0F 1A 3C 11 50 15 50 11 5B 50 3C 50 0D 04 52 0D 50 50 11 50 07 3C 52 54 1E".split()
license_key = ""

for char in secret_key:
    license_key += chr(int(char, 16) ^ 99)

print("S" + license_key)  # Flag starts with "Skill"
