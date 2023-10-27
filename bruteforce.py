import itertools
import time


start_time = time.time() * 1000


class Stock():
    def __init__(self, name, stock_price, percent_gain):
        self.name = name
        self.stock_price = stock_price
        self.percent_gain = percent_gain
        self.gain = (stock_price * percent_gain) / 100


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


def create_portfolio(list_a):
    max_total_gain = 0
    for list_of_stocks in list_a:
        portfolio = Portfolio()

        if sum(stock.stock_price for stock in list_of_stocks) <= portfolio.investment:
            for item in list_of_stocks:
                portfolio.add_stock(item)
            total_gain = portfolio.calculate_total_gain()
            if total_gain > max_total_gain:
                max_total_gain = total_gain
                yield portfolio


def best_portfolio(stocks_list: list):

    i = 2
    list_a = []
    while i < len(stocks_list):
        list_of_tulpe = itertools.combinations(stocks_list, i)
        list_a.extend(list_of_tulpe)
        i += 1

    portfolios = create_portfolio(list_a)

    sorted_portfolios = sorted(portfolios,
                               key=lambda portfolio: portfolio.calculate_total_gain(),
                               reverse=True
                               )

    portfolio = sorted_portfolios[0]
    return portfolio


stocks = [
    {"name": "Action-1", "price": 20, "profit": 5},
    {"name": "Action-2", "price": 30, "profit": 10},
    {"name": "Action-3", "price": 50, "profit": 15},
    {"name": "Action-4", "price": 70, "profit": 20},
    {"name": "Action-5", "price": 60, "profit": 17},
    {"name": "Action-6", "price": 80, "profit": 25},
    {"name": "Action-7", "price": 22, "profit": 7},
    {"name": "Action-8", "price": 26, "profit": 11},
    {"name": "Action-9", "price": 48, "profit": 13},
    {"name": "Action-10", "price": 34, "profit": 27},
    {"name": "Action-11", "price": 42, "profit": 17},
    {"name": "Action-12", "price": 110, "profit": 9},
    {"name": "Action-13", "price": 38, "profit": 23},
    {"name": "Action-14", "price": 14, "profit": 1},
    {"name": "Action-15", "price": 18, "profit": 3},
    {"name": "Action-16", "price": 8, "profit": 8},
    {"name": "Action-17", "price": 4, "profit": 12},
    {"name": "Action-18", "price": 10, "profit": 14},
    {"name": "Action-19", "price": 24, "profit": 21},
    {"name": "Action-20", "price": 114, "profit": 18},
]


stocks_list = []

for stock in stocks:
    stocks_list.append(Stock(stock["name"],
                             float(stock["price"]),
                             float(stock["profit"])
                             ))


portfolio = best_portfolio(stocks_list)

for stock in portfolio.stock_list:
    print(f"{stock.name} raporte : {stock.gain}€")
print(f"montant total des actions :{500 - portfolio.investment}€")
print("Gain total des actions apres 2 ans :",
      round(portfolio.calculate_total_gain(), 2), "€")
print("--- %s ms ---" % ((time.time()*1000) - start_time))
