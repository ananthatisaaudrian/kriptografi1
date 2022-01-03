plaintext = input("masukkan plaintext : ")
key = 0x6c
ciphertext = ""

for i in plaintext:
    ciphertext += chr(ord(i)^key)
print("Chipertext dari",plaintext,"yaitu : ", ciphertext)
ciphertext
