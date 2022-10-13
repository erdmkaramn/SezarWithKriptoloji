k=3

mesaj= input("Şifrelenecek Mesaj : ")

alfabe="abcçdefgğhıijklmnoöprsştuüvyz"

boyut=len(alfabe)

sifrelimesaj=''

for i in mesaj:
    for c in alfabe:
        if i==c:
            konum=alfabe.index(c)
            konum+=k
            sifrelimesaj+=alfabe[konum%boyut]
            
print("Şifreli: "+sifrelimesaj)