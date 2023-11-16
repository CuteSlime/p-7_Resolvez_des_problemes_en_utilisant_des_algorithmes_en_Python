import time
import csv


start_time = time.time() * 1000

MAX_INVESTMENT = 500
FILE_NAME = 'dataset2_Python+P7'


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
        self.investment = kwargs.get("investment", MAX_INVESTMENT)

    def add_stock(self, stock: object):
        self.stock_list.append(stock)
        self.investment -= stock.stock_price

    def calculate_total_gain(self):
        total_gain = 0
        for stock in self.stock_list:
            total_gain += stock.gain

        return total_gain


def csv_converter(filename: str):
    '''Convert CSV into a dictionary

    Args:
        filename (str): name of the file

    Returns:
        dict: a dictionary of stocks
    '''
    with open(f'./Data/{filename}.csv', 'r', encoding="utf-8-sig", newline="") as stocks:
        reader = csv.DictReader(
            stocks, dialect='excel', delimiter=',', quotechar='"')
        stocks = [row for row in reader if float(row['price']) > 0]

    return stocks


def optimized_portfolio(stocks_list):
    '''Main function, sort a list of stock and add stock one by one into a portfolio if not 
    exeding investment

    Args:
        stocks_list (list): list of stocks

    Returns:
        obj: a portfolio object
    '''
    sorted_stocks = sorted(stocks_list,
                           key=lambda stock: stock.ratio,
                           reverse=True
                           )
    portfolio = Portfolio()

    for stock in sorted_stocks:
        if stock.stock_price <= portfolio.investment:
            portfolio.add_stock(stock)

    return portfolio


# Main code
stocks = csv_converter(FILE_NAME)
stocks_list = [Stock(stock["name"], float(stock["price"]),
                     float(stock["profit"])) for stock in stocks]


portfolio = optimized_portfolio(stocks_list)

for stock in portfolio.stock_list:
    print(f"{stock.name} coût: { round(stock.stock_price, 2)} gain :{ round(stock.gain, 2)}€")
print(f"coût total :{round(500 - portfolio.investment, 2)}€")
print("Gain total :",
      round(portfolio.calculate_total_gain(), 2), "€")
print("--- %s ms ---" % ((time.time()*1000) - start_time))
