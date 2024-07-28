def harf_adeti(metin):
    harf_sayisi = {}
    for harf in metin:
        harf = harf.lower()
        if harf in harf_sayisi:
            harf_sayisi[harf]+=1
        else:
            harf_sayisi[harf]=1
    return harf_sayisi

toplam = 0
harfler = "abcdefghijklmnopqrstuvwxyz"
metin = (input("Metin giriniz:"))
harf_sayisi = harf_adeti(metin)

for harf,sayi in harf_sayisi.items():
    if (harf in harfler):
        toplam += sayi

for harf,sayi in harf_sayisi.items():
    if (harf in harfler):
        print(f"'{harf}' : {sayi} adet  => %{((100*sayi)/toplam):.2f}")