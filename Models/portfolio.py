class Portfolio():
    def __init__(self, **kwargs):
        self.stock_list = kwargs.get("stock_list", [])
        self.investment = kwargs.get("investment", 500)

    def add_stock(self, stock: object):
        self.stock_list.append(stock)
        self.investment -= stock.stock_price

    def calculate_total_gain(self):
        total_gain = 0
        for stock in self.stock_list:
            total_gain += stock.gain

        return total_gain
