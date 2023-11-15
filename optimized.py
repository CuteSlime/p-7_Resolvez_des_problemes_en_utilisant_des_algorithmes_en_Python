import time
import csv


start_time = time.time() * 1000


class Stock():
    def __init__(self, name, stock_price, percent_gain):
        self.name = name
        self.stock_price = stock_price
        self.percent_gain = percent_gain
        self.gain = (stock_price * percent_gain) / 100
        self.ratio = self.gain/stock_price


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


# data
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


def csv_converter(filename: str):
    with open(f'./Data/{filename}.csv', 'r', encoding="utf-8-sig", newline="") as stocks:
        reader = csv.DictReader(
            stocks, dialect='excel', delimiter=',', quotechar='"')
        stocks = [row for row in reader if float(row['price']) > 0]

    return stocks


def optimized_portfolio(stocks_list):
    sorted_stocks = sorted(stocks_list,
                           key=lambda stock: stock.ratio,
                           reverse=True
                           )
    portfolio = Portfolio()

    for stock in sorted_stocks:
        if stock.stock_price <= portfolio.investment:
            portfolio.add_stock(stock)

    return portfolio


filename = 'dataset2_Python+P7'
stocks = csv_converter(filename)
stocks_list = [Stock(stock["name"], float(stock["price"]),
                     float(stock["profit"])) for stock in stocks]


portfolio = optimized_portfolio(stocks_list)

for stock in portfolio.stock_list:
    print(f"{stock.name} coût: { round(stock.stock_price, 2)} gain :{ round(stock.gain, 2)}€")
print(f"coût total :{round(500 - portfolio.investment, 2)}€")
print("Gain total :",
      round(portfolio.calculate_total_gain(), 2), "€")
print("--- %s ms ---" % ((time.time()*1000) - start_time))
