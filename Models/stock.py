class Stock():
    def __init__(self, name, stock_price, percent_gain):
        self.name = name
        self.stock_price = stock_price
        self.percent_gain = percent_gain
        self.gain = (stock_price * percent_gain) / 100
