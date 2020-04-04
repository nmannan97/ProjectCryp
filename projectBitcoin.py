#Web driver and HTML
from selenium import webdriver
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
    
    print(arr_predict[0])
    #print(arr_prob)
    return arr_predict[0]


#class="price"
#https://cryptowat.ch/assets/btc

driver = webdriver.Ie('C:/Users/balto/OneDrive/Desktop/ProjectCrypto/IEDriverServer.exe')
driver.get('https://google.com')
#driver.get('https://cryptowat.ch/assets/btc')

text_area = driver.find_element_by_id('fakebox-text')
text_area.send_keys("https://cryptowat.ch/assets/btc")

python_button = driver.find_elements_by_xpath("fakebox-input")[0]
python_button.click()

currentDT = datetime.datetime.now()

price = []
price1 = []
time_tick = 0
while True:
    try:
        sleep(0.01)
        temp = []
        html_page = driver.page_source
        soup = BeautifulSoup(html_page, 'html.parser')
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
                data_predict_long = log_reg(price)
                data_predict_short = log_reg(price)
                print(100*(float(data_predict_short)/temp[0] - 1))
                time_tick = 0
                price1 = []
            except ValueError:
                time_tick = 0
        elif len(price) > 360000:
            price = []
        else: 
            time_tick += 1
    except KeyboardInterrupt:
        driver.close()
        break