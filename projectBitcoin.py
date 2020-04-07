#Web driver and HTML
from selenium import webdriver
from bs4 import BeautifulSoup
import urllib3
#Timing
import datetime
from time import sleep
#predictions
from sklearn.linear_model import LogisticRegression
import numpy as np
#Notifications
import win32com.client as wc 
#other
import os

speak = wc.Dispatch("Sapi.spVoice")

def log_reg(time = [], data = []):
    X = []
    temp = []
    for i in range(len(time)):
        temp.append(time[i])
        temp.append(0)
        X.append(temp)
    results = LogisticRegression().fit(X, data)
    arr_predict = np.array(results.predict(X))

    print(arr_predict[0])
    return arr_predict[0]

http = urllib3.PoolManager()
#class="price"
#https://cryptowat.ch/assets/btc

#driver = webdriver.Chrome('C:/Users/balto/OneDrive/Desktop/ProjectCrypto/ProjectCryp/chromedriver.exe')
#driver.get('https://robinhood.com/crypto/BTC')
#driver.get('https://cryptowat.ch/assets/btc')

currentDT = datetime.datetime.now()

price1 = []
time_data = []
time_tick = 0
time = 0
print('Starting...')
while True:
    try:
        r = http.request('GET','https://cryptowat.ch/assets/btc')
        sleep(1.5)
        temp = []
        html_page = r.data
        soup = BeautifulSoup(html_page, 'html.parser')
        #price_html = soup.find_all('span', class_ = 'udYkAW2UrhZln2Iv62EYb')
        price_html = soup.find_all('span', class_ = 'woobJfK-Xb2EM1W1o8yoE')
        price_html2 = price_html[0].find_all('span', class_ = 'price')
        #print(len(price_html))
        #print((price_html2))
        temp.append(time*currentDT.microsecond)
        #print(price_html2)

        temp.append((price_html2[0].contents[0]))
        #price.append(temp)
        price1.append(temp[1])
        time_data.append(temp[0])
        if time_tick == 10:
            try:
                #print('value at time t = 10, '+ str(temp[1]))
                #data_predict_long = log_reg(price)
                data_predict_short = log_reg((time_data), (price1))
                mean_error = (100*(float(data_predict_short)/float(temp[1]) - 1))
                time_tick = 0
                
                if abs(mean_error) > 0.1 and mean_error != -100.0:
                    print('mean error =  ' + str(mean_error) + '%')
                    speak.speak('warning Bitcoin check, mean error ' + str(round(mean_error, 3))) 
                time_tick = 0
            except ValueError:
                time_tick = 0
            except ZeroDivisionError:
                time_tick = 0  
        else: 
            time_tick += 1
            time+=1
        if len(price1) >500:
            price1.clear()
            time_data.clear()
            #os.system('clear')
    except KeyboardInterrupt:
        break