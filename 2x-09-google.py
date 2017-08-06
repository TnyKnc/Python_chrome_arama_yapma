#-*- coding: utf-8-*-
#3x-09-google.py

#selenium paketini yüklediktan sonra kodumuza ekliyoruz.
#Web tarayıcımızın açılması için gerekli olan modül paketi.
from selenium import webdriver
#Tarayıcıdaki arama kutusunu kullanabilmemiz için gerekli modülü ekliyoruz.
from selenium.webdriver.common.keys import Keys
#Tarayıcı açıldıktan sonra işlem yapıp hemen kapanmaması için time modülünü ekliyoruz.
import time

#gerekli işlemlerin yapılacağı fonksiyonu oluşturuyoruz.
#keyword aranacak değişkeni tutuyor.
def gogol(keyword):
    #Chrome tarayıcısının açılması için gerekli driver\'ı ekliyoruz.
    profile = webdriver.Chrome("Path/chromedriver.exe")
    #Tarayıcının açılması için bekleme süresi veriyoruz.
    profile.implicitly_wait(10)
    #girilecek sitenin adresini veriyoruz.
    searchEngineUrl="https://www.google.com.tr/"
    #Chrome tarayıcısını aç searcEngineUrl sitesine bağlan
    profile.get(searchEngineUrl)

    #Adı q olan html elemanını bul(arama kutusu)
    #!google\'a girip arama kutusunu incelediğinizde name kısmının q olduğunu göreceksiniz.
    inputElement=profile.find_element_by_name("q")

    #keyword bilgisini arama kutusuna gir ve enter tuşuna tıkla.
    inputElement.send_keys(keyword + Keys.RETURN)

    time.sleep(60) #işlemler tamamlandıktan (sayfada arama yapıldıktan) sonra 60sn bekle daha sonra tarayıcıyı kapat.

keyword="TnyKnc"
gogol(keyword) #gogol fonksiyonuna keyword değişkenini gönderiyoruz.