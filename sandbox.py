#Web driver and HTML
import urllib3
from bs4 import BeautifulSoup
#Timing
import datetime
from time import sleep
#predictions
from sklearn.linear_model import LogisticRegression
import numpy as np

sample_data = [[1, 6568.00], [2, 6763], [3, 6765], [4, 6768]]
def log_reg(data = []):
    x_data = []
    y_data = []
    temp = []
    for i in range(len(data)):
        temp.append(float(data[i][0]))
        temp.append(0)
        x_data.append(temp)
        y_data.append(data[i][1])
    
    results = LogisticRegression(random_state=0).fit(x_data, y_data)
    arr_predict = np.array(results.predict(x_data))
    #arr_prob = np.array(results.score(x_data, y_data))
    
    #print(arr_predict[0])
    #print(arr_prob)
    return arr_predict[0]

http = urllib3.PoolManager()

currentDT = datetime.datetime.now()

price = []
price1 = []
time_tick = 0
while True:
    try:
        sleep(0.01)
        temp = []
        r = http.request('GET', 'https://cryptowat.ch/assets/btc')
        soup = BeautifulSoup(r.data.decode('utf-8'), 'html.parser')
        price_html = soup.find_all('span', class_ = 'woobJfK-Xb2EM1W1o8yoE')
        price_html2 = price_html[0].find_all('span', class_ = 'price')
        #print(len(price_html))
        #print((price_html2))
        temp.append(currentDT.microsecond)
        #print(price_html2)
        temp.append(price_html2[0].contents[0])
        price.append(temp)
        if time_tick == 10:
            try:
                print(temp[1])
                data_predict_long = log_reg(price)
                data_predict_short = log_reg(price)
                print(100*(float(data_predict_short)/float(temp[1]) - 1))
                time_tick = 0
                price1 = []
            except ValueError:
                time_tick = 0
        elif len(price) > 360000:
            price = []
        else: 
            time_tick += 1
    except KeyboardInterrupt:
        break
'''
import urllib3
from bs4 import BeautifulSoup

http = urllib3.PoolManager()

for i in range(100):
    r = http.request('GET', 'https://cryptowat.ch/assets/btc')
    #print(r.data.decode('utf-8'))
    soup = BeautifulSoup(r.data.decode('utf-8'), 'html.parser')
    price_html = soup.find_all('span', class_ = 'woobJfK-Xb2EM1W1o8yoE')
    price_html2 = price_html[0].find_all('span', class_ = 'price')
    print(price_html2[0].contents[0])    
'''