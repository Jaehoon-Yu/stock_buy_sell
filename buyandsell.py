# setting class
class order:
    def __init__(self, price, order, ID, time_stamp):
        self.price = price
        self.order = order
        self.ID = ID
        self.time_stamp = time_stamp

class orderbook:
    def __init__(self):
        self.buy = []
        self.sell = []
        
    self.buy.append({})
        
