from bs4 import BeautifulSoup
import urllib.request  as urllib2 
import datetime
import time
import matplotlib.pyplot as plt
import requests as req
from selenium import webdriver, common
import re 
import win32com.client as wc 
from selenium.common import exceptions
from CryptoClasses import coins

def percent_change(name, return_val, counter, data = []):
    if counter<len(data):
        data[counter] = data[counter].replace('%', '')
        if(counter == 0):
            return_val = float(data[counter])
        else:
            return_val -= float(data[counter])
        counter += 1
        return percent_change(name, return_val, counter, data)
    else:
        return round(-return_val, 2)

def percent_change_2(data = []):
    if(len(data) == 2):       
        return float(round((1 - data[1]/data[0])*100, 5))
    else:
        return 0
        
def percent_change_3(current_percent, data = []):
    for i in range(len(data)):
        if(data[i]>current_percent):
            current_percent = data[i]
    return current_percent

speak = wc.Dispatch("Sapi.spVoice")
#speak.speak("Starting")

driver = webdriver.Chrome('C:/Users/balto/OneDrive/Desktop/ProjectCrypto/chromedriver.exe')
#driver.get('https://www.livecoinwatch.com/')

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

percent_change_val= 0.25
sample_size = 3

while(True):
    try:
        time.sleep(5.1)
        driver.get('https://www.coinbase.com/price')
        html_page = driver.page_source
        soup = BeautifulSoup(html_page, 'html.parser')
        coin = soup.find_all('h4', class_ = "TextElement__Spacer-hxkcw5-0 caIgfs Header__StyledHeader-sc-1xiyexz-0 jKklfu AssetTableRow__StyledHeader-bzcx4v-13 AssetTableRow__StyledHeaderDark-bzcx4v-15 hgGcEi")
        percentage = soup.find_all('h4', class_ = "TextElement__Spacer-hxkcw5-0 caIgfs Header__StyledHeader-sc-1xiyexz-0 gCmtXt AssetTableRow__StyledHeader-bzcx4v-13 AssetTableRow__StyledHeaderDark-bzcx4v-15 hgGcEi asset-table-percent-change")
        for i in range(len(coin)):
            if coin[i].contents[0] == coin_btc.get_name():
                temp = []
                temp_string = str(coin[i+1].contents[0])
                temp_string = temp_string.replace("$", "")
                temp_string = temp_string.replace(",", "")
                temp.append(coin[i].contents[0])
                temp.append(float(temp_string))
                temp.append(percentage[1].contents[0])
                BTC.append(temp) 
                #print(BTC)
                if len(BTC) == sample_size:
                    temp = []
                    temp2 = []
                    coin_btc.add_value(BTC)
                    for i in range(len(BTC)):
                        temp.append(BTC[i][1])
                        temp2.append(float(BTC[i][2].replace('%','')))
                    #print(temp2)
                    #print(temp)
                    print(coin_btc.percent_change_2(temp))
                    print(coin_btc.percent_change_1(temp2))
                    if(abs(coin_btc.percent_change_1(temp2))>percent_change_val or abs(coin_btc.percent_change_2(temp))>percent_change_val):
                        speak.speak("warning Bitcoin, percent change, greater than " + str(coin_btc.percent_change_1(temp2)))
                        print("BTC percent change " + str(coin_btc.percent_change_1(temp2)))
                        print("BTC percent change " + str(coin_btc.percent_change_2(temp)))
                    BTC = []
        
            elif coin[i].contents[0] == coin_doge.get_name():
                temp = []
                temp_string = str(coin[i+1].contents[0])
                temp_string = temp_string.replace("$", "")
                temp_string = temp_string.replace(",", "")
                temp.append(coin[i].contents[0])
                temp.append(float(temp_string))
                temp.append(percentage[33].contents[0])
                DOGE.append(temp)
                if len(DOGE) == sample_size:
                    temp = []
                    temp2 = []
                    coin_doge.add_value(DOGE)
                    print(coin_btc.percent_change_2(temp))
                    for i in range(len(DOGE)):
                        temp.append(DOGE[i][1])
                        temp2.append(float(DOGE[i][2].replace('%','')))
                    if(abs(coin_btc.percent_change_1(temp2))>percent_change_val or abs(coin_btc.percent_change_2(temp))>percent_change_val):
                        speak.speak("warning Dogecoin, percent change, greater than " + str(coin_doge.percent_change_1(temp2)))
                        print("DOGE percent change " + str(coin_doge.percent_change_1(temp2)))
                        print("DOGE percent change " + str(coin_doge.percent_change_2(temp)))
                    DOGE = []
            
            elif coin[i].contents[0] == coin_eth.get_name():
                temp = []
                temp_string = str(coin[i+1].contents[0])
                temp_string = temp_string.replace("$", "")
                temp_string = temp_string.replace(",", "")
                temp.append(coin[i].contents[0])
                temp.append(float(temp_string))
                temp.append(percentage[2].contents[0])
                ETH.append(temp)
                if len(ETH) == sample_size:
                    temp2 = []
                    temp = []
                    coin_eth.add_value(ETH)
                    for i in range(len(ETH)):
                        temp.append(ETH[i][1])
                        temp2.append(float(ETH[i][2].replace('%','')))
                    if(abs(coin_btc.percent_change_1(temp2))>percent_change_val or abs(coin_btc.percent_change_2(temp))>percent_change_val):
                        speak.speak("warning Ethereum, percent change, greater than " + str(coin_eth.percent_change_1(temp2)))
                        print("ETH percent change " + str(coin_eth.percent_change_1(temp2)))
                        print("ETH percent change " + str(coin_eth.percent_change_2(temp)))
                    ETH = []

            elif coin[i].contents[0] == coin_etc.get_name():
                temp = []
                temp_string = str(coin[i+1].contents[0])
                temp_string = temp_string.replace("$", "")
                temp_string = temp_string.replace(",", "")
                temp.append(coin[i].contents[0])
                temp.append(float(temp_string))
                temp.append(percentage[21].contents[0])
                ETC.append(temp)
                if len(ETC) == sample_size:
                    temp2 = []
                    temp = []

                    coin_etc.add_value(ETC)
                    for i in range(len(ETC)):
                        temp.append(ETC[i][1])
                        temp2.append(float(ETC[i][2].replace('%','')))
                    if(abs(coin_btc.percent_change_1(temp2))>percent_change_val or abs(coin_btc.percent_change_2(temp))>percent_change_val):
                        speak.speak("warning Ethereum Classic, percent change, greater than " + str(coin_etc.percent_change_1(temp2)))
                        print("ETC percent change " + str(coin_etc.percent_change_1(temp2)))
                        print("ETC percent change " + str(coin_etc.percent_change_2(temp)))
                    ETC = []

            elif coin[i].contents[0] == coin_bsv.get_name():
                temp = []
                temp_string = str(coin[i+1].contents[0])
                temp_string = temp_string.replace("$", "")
                temp_string = temp_string.replace(",", "")
                temp.append(coin[i].contents[0])
                temp.append(float(temp_string))
                temp.append(percentage[6].contents[0])
                BSV.append(temp)
                if len(BSV) == sample_size:
                    temp2 = []
                    temp = []
                    print(coin_bsv.percent_change_2(temp))
                    coin_bsv.add_value(BSV)
                    for i in range(len(BSV)):
                        temp.append(BSV[i][1])
                        temp2.append(float(BSV[i][2].replace('%','')))
                    if(abs(coin_bsv.percent_change_1(temp2))>percent_change_val or abs(coin_bsv.percent_change_2(temp))>percent_change_val):
                        speak.speak("warning Bitcoin SV, percent change, greater than " + str(coin_bsv.percent_change_1(temp2)))
                        print("BSV percent change " + str(coin_bsv.percent_change_1(temp2)))
                        print("BSV percent change " + str(coin_bsv.percent_change_2(temp)))
                    BSV = []
            
            elif coin[i].contents[0] == coin_ltc.get_name():
                temp = []
                temp_string = str(coin[i+1].contents[0])
                temp_string = temp_string.replace("$", "")
                temp_string = temp_string.replace(",", "")
                temp.append(coin[i].contents[0])
                temp.append(float(temp_string))
                temp.append(percentage[7].contents[0])
                BSV.append(temp)
                if len(LTC) == sample_size:
                    temp2 = []
                    temp = []
                    coin_ltc.add_value(LTC)
                    print(coin_ltc.percent_change_2(temp))
                    for i in range(len(LTC)):
                        temp.append(LTC[i][1])
                        temp2.append(float(LTC[i][2].replace('%','')))
                    if(abs(coin_btc.percent_change_1(temp2))>percent_change_val or abs(coin_btc.percent_change_2(temp))>percent_change_val):
                        speak.speak("warning Litecoin, percent change, greater than " + str(coin_ltc.percent_change_1(temp2)))
                        print("LTC percent change " + str(coin_ltc.percent_change_1(temp2)))
                        print("LTC percent change " + str(coin_ltc.percent_change_2(temp)))
                    LTC = []

    except KeyboardInterrupt:
        driver.close()
        break
    except IndexError:
        continue


driver.close()

'''      
<h4 class="TextElement__Spacer-hxkcw5-0 caIgfs Header__StyledHeader-sc-1xiyexz-0 jKklfu AssetTableRow__StyledHeader-bzcx4v-13 AssetTableRow__StyledHeaderDark-bzcx4v-15 hgGcEi">$6,691.25</h4>
'''