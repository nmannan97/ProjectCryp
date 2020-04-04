from bs4 import BeautifulSoup
from selenium.common import exceptions
from selenium import webdriver, common

import time

import win32com.client as wc 

from CryptoClasses import coins

speak = wc.Dispatch("Sapi.spVoice")
#speak.speak("Starting")

driver = webdriver.Chrome('C:/Users/balto/OneDrive/Desktop/ProjectCrypto/chromedriver.exe')
driver.get('https://www.livecoinwatch.com/')

BTC = []
DOGE = []
ETH = []
ETC = []
BSV = []
LTC = []

ticks = []

coin_btc = coins('Bitcoin', 0, 0, BTC)
coin_doge = coins('Dogecoin', 0, 0, DOGE)
coin_eth = coins('Ethereum',0,0, ETH)
coin_etc = coins("Ethereum Classic",0 ,0 ,ETC)
coin_bsv = coins("Bitcoin SV", 0, 0, BSV)
coin_ltc = coins('Litecoin', 0, 0, LTC)

percent_change_val= 0.01
sample_size = 3

while True:
    try:
        html_page = driver.page_source
        soup = BeautifulSoup(html_page, 'html.parser')
        data = soup.find_all('tr', class_ = "table-row filter-row table-row")
        for i in range(len(data)):
            coin = data[i].find_all('small', class_ = 'abr text-truncate')
            for j in range(len(coin)):
                if coin[j].contents[0] == 'Bitcoin':
                    temp = []
                    price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                    percent = data[i].find_all('span', class_ = 'percent')
                    temp.append(price[1].contents[2])
                    temp.append(percent[0].contents[0])
                    BTC.append(temp)
                    if len(BTC) == 120:
                        temp2 = []
                        temp1 = []
                        for k in range(len(BTC)):
                            temp2.append(BTC[k][0])
                            temp1.append(float(BTC[k][1].replace('%', '')))
                            #print(temp1)
                        print(coin_btc.percent_change_2(temp2))
                        print(coin_btc.percent_change_1(temp1))
                        if(abs(coin_btc.percent_change_2(temp2))>percent_change_val or abs(coin_btc.percent_change_1(temp1))>percent_change_val):
                            speak.speak("Warning Bitcoin percent change is " + str(round(coin_btc.percent_change_2(temp2),3)))
                            print("BTC percent change: " + str(round(coin_btc.percent_change_2(temp2),3)))
                            print("BTC price change: " + str(round(coin_btc.percent_change_1(temp1),3)))
                        BTC = []
                elif coin[j].contents[0] == 'Bitcoin SV':
                    temp = []
                    price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                    percent = data[i].find_all('span', class_ = 'percent')
                    temp.append(price[1].contents[2])
                    temp.append(percent[0].contents[0])
                    BSV.append(temp)
                    if len(BTC) == 120:
                        temp2 = []
                        temp1 = []
                        for k in range(len(BTC)):
                            temp2.append(BTC[k][0])
                            temp1.append(float(BTC[k][1].replace('%', '')))
                            #print(temp1)
                        print(coin_btc.percent_change_2(temp2))
                        print(coin_btc.percent_change_1(temp1))
                        if(abs(coin_btc.percent_change_2(temp2))>percent_change_val or abs(coin_btc.percent_change_1(temp1))>percent_change_val):
                            speak.speak("Warning Bitcoin SV percent change is " + str(round(coin_btc.percent_change_2(temp2),3)))
                            print("BTC percent change: " + str(round(coin_btc.percent_change_2(temp2),3)))
                            print("BTC price change: " + str(round(coin_btc.percent_change_1(temp1),3)))
                        BSV = []
    except KeyboardInterrupt:
        driver.close()
        break