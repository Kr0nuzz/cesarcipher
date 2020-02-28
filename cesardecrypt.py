import os

upper = list("ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ")
lower = list("abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz")
undefine = list("`1234567890~!@#$%^&*()-+=_{}[];:' `1234567890~!@#$%^&*()-+=_{}[];:' ")


def banner():
    print("""                                                      
                ▒▒▒▒▒▒                                                        
              ▒▒▒▒▒▒▒▒▒▒                                                      
            ▒▒▒▒      ▒▒▒▒                                                    
            ▒▒▒▒      ▒▒▒▒                                                    
            ▒▒▒▒      ▒▒▒▒                          ████████                  
          ██████████████████                      ██▓▓▓▓▓▓▓▓██                
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██████████████████▓▓████▓▓██                
        ██▓▓▓▓▓▓██████▓▓▓▓▓▓██  ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓████▓▓██                
        ██▓▓▓▓▓▓██████▓▓▓▓▓▓██  ██▓▓██▓▓████████████▓▓████▓▓██                
        ██▓▓▓▓▓▓▓▓██▓▓▓▓▓▓▓▓██  ██▓▓██▓▓██        ██▓▓▓▓▓▓▓▓██                
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    ██  ██            ████████                  
        ██▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓██    Author : Kr0nuzz                                            
          ██████████████████      Purpose : Enc & Decrypt Cesarchiper                                            
                              _     _       _               
  ___ ___  ___  __ _ _ __ ___| |__ (_)_ __ | |__   ___ _ __ 
 / __/ _ \/ __|/ _` | '__/ __| '_ \| | '_ \| '_ \ / _ \ '__|
| (_|  __/\__ \ (_| | | | (__| | | | | |_) | | | |  __/ |   
 \___\___||___/\__,_|_|  \___|_| |_|_| .__/|_| |_|\___|_|   
                                     |_|                    
""")
    print("[1] Encrypt Code")
    print("[2] Decrypt Code")


def tit():
    plaintext1 = input("Masukkan kata yang ingin di encrypt: ")
    key1 = int(input("Masukkan Key: "))
    def enc(plaintext1, key1):
        res = []
        for i in plaintext1:
            if i in lower:
                en = lower.index(i)+key1
                res.append(lower[en])
            elif i in upper:
                en = upper.index(i)+key1
                res.append(upper[en])
            elif i in undefine:
                en = undefine.index(i)
                res.append(undefine[en])
            else:
                print("Kamu Salah Input!!")
        return "".join(res)
    print("Hasil >> ", enc(plaintext1,key1))

def tut():
    key = 1
    plaintext = input("Masukkan kata yang ingin di decrypt: ")
    def dec(plaintext, key):
        res = []
        for i in plaintext:
            if i in lower:
                dex = lower.index(i)-key
                res.append(lower[dex])
            elif i in upper:
                dex = lower.index(i)-key
                res.append(upper[dex])
            elif i in undefine:
                dex = undefine.index(i)
                res.append(undefine[dex])
            else:
                res.append(i)
        return "".join(res)
    for r in range(26):
        print(str(r)+":", dec(plaintext, key+r))
    print("Pilih Kata yang bisa dipahami")
if __name__=="__main__":
    try:
        os.system("clear")
        banner()
        p = int(input("Masukkan Pilihan >> "))
        if p == 1:
            tit()
        elif p == 2:
            tut()
        else:
            print("Kamu Salah Input!!")
    except ValueError:
        print("Kamu salah input!!")
