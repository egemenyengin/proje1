#import I2C_LCD_driver
from time import *
import time
import sqlite3
import feedparser
import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint
scope = ['https://spreadsheets.google.com/feeds']
creds = ServiceAccountCredentials.from_json_keyfile_name('kiyafetstok-5bb00f1ff518.json', scope)
client = gspread.authorize(creds)
sheet = client.open('kiyafetstok').sheet1


kiyafet1=['2736180947', range(0,5)]
kiyafet2=['1386361917', range(5,10)]
kiyafet3=['2032263926', range(10,15)]
kiyafet4=['3655052005', range(15,20)]

def fonksiyonlar():

    conn = sqlite3.connect('kiyafetler1.db')


    sec=int(input("Yapacağınız işlemi seçin: \n 1. Kıyafet Ekle\n 2. Kıyafet Çıkar\n 3.Kıyafet Önerisi\n 4.Hava Durumu\n 5.Stogunuz:\n"))
    if sec==1:
        girisekrani()
    elif sec==2:
        kiyafetcikar()
    elif sec==3:
        kiyafetonerisi()
        sleep(3)
        fonksiyonlar()
    elif sec==4:
        hava()
        sleep(3)
        fonksiyonlar()
    elif sec==5:
        stokkontrol()
        sleep(3)
        fonksiyonlar()
    else:
        print("İşlem seçmediniz")
        sleep(1)
        fonksiyonlar()


def girisekrani():
    giris=input("kiyafeti gir, çıkmak için kartını okut: ")
    if giris == str(kiyafet1[0]):
        print("Kiyafet1")
        row = ["Kiyafet1", "2736180947", "0", "v"]
        index = 1
        sheet.insert_row(row, index)
        print("yerlestirildi.")
        girisekrani()
    elif giris==str(kiyafet2[0]):
        print("Kiyafet2")
        row = ["Kiyafet2", "1386361917", "5", "v"]
        index = 2
        sheet.insert_row(row, index)
        print("yerlestirildi.")
        girisekrani()
    elif giris==str(kiyafet3[0]):
        print("Kiyafet3")
        row = ["Kiyafet3", "2032263926", "10", "v"]
        index = 3
        sheet.insert_row(row, index)
        print("yerlestirildi.")
        girisekrani()
    elif giris==str(kiyafet4[0]):
        print("Kiyafet4")
        row = ["Kiyafet4", "3655052005", "15", "v"]
        index = 4
        sheet.insert_row(row, index)
        print("yerlestirildi.")
        girisekrani()
    elif giris==str(2456326148):
        hava()
    else:
        print("tanimlanmamis")
        girisekrani()

    return

def kiyafetcikar():

    giris=input("kiyafeti gir, çıkmak için kartını okut: ")
    if giris == kiyafet1[0]:
        print("Kiyafet1")
        sheet.delete_row(1)
    elif giris==kiyafet2[0]:
        print("Kiyafet2")
        sheet.delete_row(2)
    elif giris==kiyafet3[0]:
        print("Kiyafet3")
        sheet.delete_row(3)
    elif giris==kiyafet4[0]:
        print("Kiyafet4")
        sheet.delete_row(4)
    elif giris==str(2456326148):
        hava()
    else:
        print("tanimlanmamis")
    print("cikartildi")

    return hava()


def kiyafetonerisi():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|34722|ISTANBUL|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    if int(parse[4]) in range(0, 5):
        print("Kıyafet1 giyilebilir")
    elif int(parse[4]) in range(5, 10):
        print("Kiyafet2 giyilebilir")
    elif int(parse[4]) in range(10, 15):
        print("Kiyafet3 giyilebilir")
    elif int(parse[4]) in range(15, 20):
        print("Kiyafet4 giyilebilir")
    else:
        print("Bu havaya göre kıyafetiniz yok...")
    return

def kontrol():
    kontrolkodu=int(input("Hoşgeldiniz; giriş için kartınızı okutunuz: \t"))
    if kontrolkodu==2456326148:
        print("Doğru şifre!")
        sleep(1)

        fonksiyonlar()

    else:
        print("Yanlış şifre, tekrar deneyiniz")
        sleep(1)
        kontrol()
    return kontrolkodu

def stokkontrol():


    results = sheet.cell(1,4).value + sheet.cell(2,4).value + sheet.cell(3,4).value + sheet.cell(4,4).value
    i=0
    for y in results:
        i+=1

    print("Dolabınızda", i, "adet kiyafet mevcut")


def hava():
    while True:
        gun = datetime.datetime.now().strftime("%d");
        ay  = datetime.datetime.now().strftime("%m");
        yil = datetime.datetime.now().strftime("%Y");
        saat = datetime.datetime.now().strftime("%H");
        dakika = datetime.datetime.now().strftime("%M");
        tarih=gun+"."+ay+"."+yil+" "+saat+":"+dakika
        parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|34722|ISTANBUL|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        havad=parse[2] + parse[4] + "*C"
        print(tarih, havad)
        #mylcd.lcd_display_string(tarih, 2)
        #mylcd.lcd_display_string(havad, 1)
        sleep(10)
        test=input("")
        if bool(test)==True:
            fonksiyonlar()
        else:
            hava()
        return(hava)

kontrol()

