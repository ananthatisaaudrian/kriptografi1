print("========ENKRIPSI==========")


plain = input("Masukkan Plaintext : ")
key = 0x6c
cipher = ""



for i in plain:
    cipher += chr(ord(i)^key)
print("Chipertext dari",plain," adalah = ", cipher)
cipher
