ciphertext = input("Masukkan Chipertext : ") 
key = 0x61
plaintext= ""

for i in ciphertext:
    plaintext += chr(ord(i)^key)
print("Plaintextnya yaitu : ", plaintext)
plaintext
