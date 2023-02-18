from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP

# public key is given
n = 114381625757888867669235779976146612010218296721242362562561842935706935245733897830597123563958705058989075147599290026879543541
e = 9007

# ciphered output
cipher_text = eval(open('output.txt').read())

# factorized N using factordb.com
p = 3490529510847650949147849619903898133417764638493387843990820577
q = 32769132993266709549961988190834461413177642967992942539798288533

phi = (p - 1) * (q - 1)

# modular multiplicative inverse
d = pow(e, -1, phi)

private_key = RSA.construct((n, e, d))
decryptor = PKCS1_OAEP.new(private_key)
decrypted = decryptor.decrypt(cipher_text)  # Flag starts with "Skill"
print(decrypted.decode('utf-8'))
