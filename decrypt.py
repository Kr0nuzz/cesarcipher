L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

ciphertext = input("Masukkan Teks>> ")
key = int(input("Masukkan Key>> "))

#output
plaintext2 = ""
for c in ciphertext.upper():
    if c.isalpha():
        plaintext2 += I2L[ (L2I[c] - key)%26 ]

print(plaintext2)

