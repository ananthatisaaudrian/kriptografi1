print("========DESKRIPSI==========")

cipher = input("Masukkan Chipertext = ") 
key = 0x6c
plain= ""



for i in cipher:
    plain += chr(ord(i)^key)
print("Plaintextnya adalah = ", plain)
plain
