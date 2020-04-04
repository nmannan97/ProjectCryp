import sklearn 

class coins():

    def __init__(self, name, price_start, percent_start, data_array = []):
        self.name = name
        self.price_start = price_start
        self.percent_start = percent_start
        self.data_array = []
    
    def percent_change_1(self, data = []):
        max_percent = 0
        temp = 0
        for i in range(1, len(data)):
            temp = float(data[0]) - float(data[i])
            if(temp != 0 and temp>max_percent):
                max_percent = temp

        return round(max_percent, 3)

    def percent_change_2(self,data = []):
        max_percent = 0
        temp = 0
        for i in range(len(data)):  
            temp = (float(data[i])/float(data[0])-1)*100
            if abs(temp) > max_percent:
                max_percent = temp
        return max_percent

    def add_value(self, value = []):
        self.data_array.append(value)

    def get_name(self):
        return self.name

    def get_prices(self):
        return self.data_array
    
    def gradient_descent(self):

        return 0