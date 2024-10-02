#Türkçe karakterlere dikkat ederek küçük harfe çeviren fonksiyon
def formatDomain (domain):
    turkish_lower_map=  str.maketrans("IİŞĞÜÇÖ","ıişğüçö")
    return domain.translate(turkish_lower_map).lower()

#Alan adı
domain1 = "EXAMPLE1.COM"
domain2 = "EXAMPLE2.COM"
domain3 = "EXAMPLE3.COM"
domain4 = "TEST1.COM"
domain5 = "TEST2.COM"
domain6 = "TEST3.COM"
domain7 = "TEST.COM"
domain8 = "DOMAIN1.COM"
domain9 = "DOMAIN9.COM"
domain10 = "SAMPLE1.COM"
domain11 = "SAMPLE2.COM"
domain12 = "SİTE1.COM"
domain13 = "SİTE2.COM"
domain14 = "WEB1.COM"
domain15 = "WEB2.COM"
domain16 = "WEB3.COM"
domain17 = "WEB4.COM"
domain18 = "WEB16.COM"
domain19 = "ADDRESS19.COM"
domain20 = "ADDRESS20.COM"

# Sonuçları ekrana yazdıran
print(domain1)
print(domain2)
print(domain3)
print(domain4)
print(domain5)
print(domain6)
print(domain7)
print(domain8)
print(domain9)
print(domain10)
print(domain11)
print(domain12)
print(domain13)
print(domain14)
print(domain15)
print(domain16)
print(domain17)
print(domain18)
print(domain19)
print(domain20)


