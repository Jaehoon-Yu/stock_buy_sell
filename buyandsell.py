# setting class
class order:
    def __init__(self, price, side, time_stamp):
        self.price = price
        self.side = side
        self.time_stamp = time_stamp

#adding order
class orderbook:
    def __init__(self):
        self.buy = []
        self.sell = []
        
    def add_order(self):
        if self.side == buy:
            self.buy.append({})
            
        elif self.side == sell:
            self.sell.append({})
        

        
