import random

def deneme(kapilari_degis, kapilar=3):
    secilen_kapi = random.randint(1, kapilar)
    if kapilari_degis:
        gosterilen_kapi = 3 if secilen_kapi==2 else 2
        mevcu_kapilar = [x for x in range(1,kapilar+1) if x not in (secilen_kapi, gosterilen_kapi)]
        secilen_kapi = random.choice(mevcu_kapilar)
    return secilen_kapi == 1

def deneme2(deneme_sayisi, kapilari_degis, kapilar=3):

    nwins = 0
    for i in range(deneme_sayisi):
        if deneme(kapilari_degis, kapilar):
            nwins += 1
    return nwins

kapilar, deneme_sayisi = 3, 100000
degisimsiz_kazanma = deneme2(deneme_sayisi, False, kapilar)
degisimli_kazanma = deneme2(deneme_sayisi, True, kapilar)

print('{} kapı ile Monty Hall Problemi'.format(kapilar))
print('Kapıyı değiştirmediğinizdeki şansınız: {:.4f}%'
            .format(degisimsiz_kazanma/deneme_sayisi * 100))
print('Kapıyı değiştirdiğinizde şansınız: {:.4f}%'
            .format(degisimli_kazanma/deneme_sayisi * 100))

#https://youtu.be/UgAnTPLA8NA
