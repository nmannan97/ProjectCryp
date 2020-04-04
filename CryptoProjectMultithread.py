#Webscraping
from bs4 import BeautifulSoup
from selenium import webdriver, common
from selenium.common import exceptions
#timing
from time import sleep
#speach
import win32com.client as wc
import os
#Custom class
from CryptoClasses import coins
#threading
import threading 
import pythoncom


speak = wc.Dispatch("Sapi.spVoice")

driver = webdriver.Chrome('C:/Users/balto/OneDrive/Desktop/ProjectCrypto/chromedriver.exe')
driver.get('https://www.livecoinwatch.com/')

BTC = []
BSV = []
ETH = []
ETC = []
LTC = []
DOGE = []

coin_btc = coins('BTC',0 , 0, BTC)
coin_bsv = coins('BSV',0 , 0, BSV)
coin_eth = coins('ETH',0 , 0, ETH)
coin_etc = coins('ETC',0 , 0, ETC)
coin_ltc = coins('LTC',0 , 0, LTC)
coin_doge = coins('DOGE',0 , 0, DOGE)

percent_change_val = 0.2

def Bitcoin():
    global BTC
    global coin_btc
    global speak
    pythoncom.CoInitialize()
    #test = http.request('GET', 'https://www.livecoinwatch.com/')
    while(True):
        #sleep(0.01)
        try:
            temp = []
            html_page = driver.page_source
            soup = BeautifulSoup(html_page, 'html.parser')
            data = soup.find_all('tr', class_ = "table-row filter-row table-row")
            for i in range(len(data)):
                coin = data[i].find_all('small', class_ = 'abr text-truncate')
                for j in range(len(coin)):
                    if coin[j].contents[0] == 'Bitcoin':
                        price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                        percent = data[i].find_all('span', class_ = 'percent')
                        temp.append(price[1].contents[2])
                        temp.append(percent[0].contents[0])
                        BTC.append(temp)
                        if len(BTC) == 60:
                            #print(BTC)
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
                        #print(BTC[0][0])
        except KeyboardInterrupt:
            driver.close()
            break

def Bitcoin_SV():
    global BSV
    global coin_bsv
    global speak
    pythoncom.CoInitialize()
    while(True):
        #sleep(0.01)
        try:
            temp = []
            html_page = driver.page_source
            soup = BeautifulSoup(html_page, 'html.parser')
            data = soup.find_all('tr', class_ = "table-row filter-row table-row")
            for i in range(len(data)):
                coin = data[i].find_all('small', class_ = 'abr text-truncate')
                for j in range(len(coin)):
                    if coin[j].contents[0] == 'Bitcoin SV':
                        price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                        percent = data[i].find_all('span', class_ = 'percent')
                        temp.append(price[1].contents[2])
                        temp.append(percent[0].contents[0])
                        BSV.append(temp)
                        if len(BSV) == 60:
                            #print(BSV[0][0])
                            temp2 = []
                            temp1 = []
                            
                            for k in range(len(BSV)):
                                temp2.append(BSV[k][0])
                                temp1.append(float(BSV[k][1].replace('%', '')))
                            if(abs(coin_bsv.percent_change_2(temp2))>percent_change_val or abs(coin_bsv.percent_change_1(temp1))>percent_change_val):
                                speak.speak("Warning Bitcoin SV percent change is " + str(round(coin_bsv.percent_change_2(temp2),3)))
                                print("BSV percent change: " + str(round(coin_bsv.percent_change_2(temp2),3)))
                                print("BSV price change: " + str(round(coin_bsv.percent_change_1(temp1),3)))
                            BSV = []
        except KeyboardInterrupt:
            driver.close()
            break

def Ethereum():
    global ETH
    global coin_eth
    global speak
    pythoncom.CoInitialize()
    while(True):
        #sleep(0.01)
        try:
            temp = []
            html_page = driver.page_source
            soup = BeautifulSoup(html_page, 'html.parser')
            data = soup.find_all('tr', class_ = "table-row filter-row table-row")
            for i in range(len(data)):
                coin = data[i].find_all('small', class_ = 'abr text-truncate')
                for j in range(len(coin)):
                    if coin[j].contents[0] == 'Ethereum':
                        price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                        percent = data[i].find_all('span', class_ = 'percent')
                        temp.append(price[1].contents[2])
                        temp.append(percent[0].contents[0])
                        ETH.append(temp)
                        if len(ETH) == 60:
                            temp2 = []
                            temp1 = []
                            for k in range(len(ETH)):
                                temp2.append(ETH[k][0])
                                temp1.append(float(ETH[k][1].replace('%', '')))
                            if(abs(coin_eth.percent_change_2(temp2))>percent_change_val or abs(coin_eth.percent_change_1(temp1))>percent_change_val):
                                speak.speak("Warning Ethereum percent change is " + str(round(coin_eth.percent_change_2(temp2),3)))
                                print("ETH percent change: " + str(round(coin_eth.percent_change_2(temp2),3)))
                                print("ETH price change: " + str(round(coin_eth.percent_change_1(temp1),3)))
                            ETH = []
        except KeyboardInterrupt:
            driver.close()
            break

def Ethereum_Classic():
    global ETC
    global coin_etc
    global speak
    pythoncom.CoInitialize()
    while(True):
        #sleep(0.01)
        try:
            temp = []
            html_page = driver.page_source
            soup = BeautifulSoup(html_page, 'html.parser')
            data = soup.find_all('tr', class_ = "table-row filter-row table-row")
            for i in range(len(data)):
                coin = data[i].find_all('small', class_ = 'abr text-truncate')
                for j in range(len(coin)):
                    if coin[j].contents[0] == 'Ethereum Classic':
                        price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                        percent = data[i].find_all('span', class_ = 'percent')
                        temp.append(price[1].contents[2])
                        temp.append(percent[0].contents[0])
                        ETC.append(temp)
                        if len(ETC) == 60:
                            temp2 = []
                            temp1 = []
                            for k in range(len(ETC)):
                                temp2.append(ETC[k][0])
                                temp1.append(float(ETC[k][1].replace('%', '')))
                            if(abs(coin_etc.percent_change_2(temp2))>percent_change_val or abs(coin_etc.percent_change_1(temp1))>percent_change_val):
                                speak.speak("Warning Ethereum Classic percent change is " + str(round(coin_etc.percent_change_2(temp2),3)))
                                print("ETC percent change: " + str(round(coin_etc.percent_change_2(temp2),3)))
                                print("ETC price change: " + str(round(coin_etc.percent_change_1(temp1),3)))
                            ETC = []
        except KeyboardInterrupt:
            driver.close()
            break

def Litecoin():
    global LTC
    global coin_ltc
    global speak
    pythoncom.CoInitialize()
    while(True):
        #sleep(0.01)
        try:
            temp = []
            html_page = driver.page_source
            soup = BeautifulSoup(html_page, 'html.parser')
            data = soup.find_all('tr', class_ = "table-row filter-row table-row")
            for i in range(len(data)):
                coin = data[i].find_all('small', class_ = 'abr text-truncate')
                for j in range(len(coin)):
                    if coin[j].contents[0] == 'Litecoin':
                        price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                        percent = data[i].find_all('span', class_ = 'percent')
                        temp.append(price[1].contents[2])
                        temp.append(percent[0].contents[0])
                        LTC.append(temp)
                        if len(LTC) == 60:
                            temp2 = []
                            temp1 = []
                            for k in range(len(LTC)):
                                temp2.append(LTC[k][0])
                                temp1.append(float(LTC[k][1].replace('%', '')))
                            if(abs(coin_ltc.percent_change_2(temp2))>percent_change_val or abs(coin_ltc.percent_change_1(temp1))>percent_change_val):
                                speak.speak("Warning Litecoin percent change is " + str(round(coin_ltc.percent_change_2(temp2),3)))
                                print("LTC percent change: " + str(round(coin_ltc.percent_change_2(temp2),3)))
                                print("LTC price change: " + str(round(coin_ltc.percent_change_1(temp1),3)))
                            LTC = []
        except KeyboardInterrupt:
            driver.close()
            break

def Dogecoin():
    global DOGE
    global coin_doge
    global speak
    pythoncom.CoInitialize()
    while(True):
        #sleep(0.01)
        try:
            temp = []
            html_page = driver.page_source
            soup = BeautifulSoup(html_page, 'html.parser')
            data = soup.find_all('tr', class_ = "table-row filter-row table-row")
            for i in range(len(data)):
                coin = data[i].find_all('small', class_ = 'abr text-truncate')
                for j in range(len(coin)):
                    if coin[j].contents[0] == 'Dogecoin':
                        price = (data[i].find_all('td', class_ = 'filter-item table-item'))
                        percent = data[i].find_all('span', class_ = 'percent')
                        temp.append(price[1].contents[2])
                        temp.append(percent[0].contents[0])
                        DOGE.append(temp)
                        if len(DOGE) == 60:
                            temp2 = []
                            temp1 = []
                            for k in range(len(DOGE)):
                                temp2.append(DOGE[k][0])
                                temp1.append(float(DOGE[k][1].replace('%', '')))
                            if(abs(coin_doge.percent_change_2(temp2))>percent_change_val or abs(coin_doge.percent_change_1(temp1))>percent_change_val):
                                speak.speak("Warning Dogecoin percent change is " + str(round(coin_doge.percent_change_2(temp2),3)))
                                print("DOGE percent change: " + str(round(coin_doge.percent_change_2(temp2),3)))
                                print("DOGE price change: " + str(round(coin_doge.percent_change_1(temp1),3)))
                            DOGE = []
        except KeyboardInterrupt:
            driver.close()
            break
    
if __name__ == "__main__": 
  
    # creating threads 
    t1 = threading.Thread(target=Bitcoin, name='t1') 
    t2 = threading.Thread(target=Bitcoin_SV, name='t2')
    t3 = threading.Thread(target=Ethereum, name='t3')
    t4 = threading.Thread(target=Ethereum_Classic, name='t4')
    t5 = threading.Thread(target=Litecoin, name='t5')
    t6 = threading.Thread(target=Dogecoin, name='t6')   
  
    # starting threads 
    t1.start() 
    t2.start()
    t3.start() 
    t4.start() 
    t5.start() 
    t6.start()  
  
    #joining threads
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()
    t6.join()