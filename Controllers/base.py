import time
import csv
from Models.stock import Stock
from Models.portfolio import Portfolio
start_time = time.time()*1000


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


class Controller():
    def __init__(self, view):
        self.view = view

    def csv_converter(self, filename: str):
        with open(f'./Data/{filename}.csv', 'r', encoding="utf-8-sig", newline="") as stocks:
            reader = csv.DictReader(
                stocks, dialect='excel', delimiter=',', quotechar='"')
            stocks = [row for row in reader if float(row['price']) > 0]

        return stocks

    def optimized_portfolio(self, stocks_list):
        sorted_stocks = sorted(stocks_list,
                               key=lambda stock: stock.percent_gain,
                               reverse=True
                               )
        portfolio = Portfolio()

        for stock in sorted_stocks:
            if stock.stock_price <= portfolio.investment:
                portfolio.add_stock(stock)

        return portfolio

    def create_portfolio_list(self, list_a):
        max_total_gain = 0
        best_portfolio = ""
        for list_of_stocks in list_a:
            portfolio = Portfolio()
            total_price = sum(stock.stock_price for stock in list_of_stocks)

            if total_price <= portfolio.investment:
                for item in list_of_stocks:
                    portfolio.add_stock(item)
                total_gain = portfolio.calculate_total_gain()
                if total_gain > max_total_gain:
                    max_total_gain = total_gain
                    best_portfolio = portfolio
        return best_portfolio

    def bruteforce_portfolio(self, stocks_list: list):

        i = 2
        list_a = []
        while i < len(stocks_list)+1:
            list_of_tulpe = self.combinations(stocks_list, i, 500)
            list_a.extend(list_of_tulpe)
            i += 1

        portfolio = self.create_portfolio_list(list_a)

        return portfolio

    def combinations(self, iterable, group_by, investment):

        pool = tuple(iterable)
        n = len(pool)
        if group_by > n:
            return
        indices = list(range(group_by))
        stocks_price = 0
        old_stocks_gain = 0
        stocks_gain = 0
        ratio = 0
        for i in indices:
            stocks_price += pool[i].stock_price
            stocks_gain += pool[i].gain
        if stocks_price > 0:
            ratio = stocks_gain / stocks_price
        base_ratio = ratio

        if stocks_price <= investment:
            old_stocks_gain = stocks_gain
            yield tuple(pool[i] for i in indices)

        while True:
            stocks_price = 0
            stocks_gain = 0
            ratio = 0
            for i in reversed(range(group_by)):
                if indices[i] != i + n - group_by:
                    break
            else:
                return
            indices[i] += 1
            for j in range(i+1, group_by):
                indices[j] = indices[j-1] + 1
            for i in indices:
                stocks_price += pool[i].stock_price
                stocks_gain += pool[i].gain

            if stocks_price > 0:
                ratio = stocks_gain / stocks_price

            if stocks_price <= investment and ratio >= base_ratio:

                if stocks_gain >= old_stocks_gain:
                    old_stocks_gain = stocks_gain
                    base_ratio = ratio
                    yield tuple(pool[i] for i in indices)

    def run(self):

        stocks_list = []
        filename = 'dataset1_Python+P7 copy'
        stocks = self.csv_converter(filename)
        for stock in stocks:
            stocks_list.append(Stock(stock["name"],
                                     float(stock["price"]),
                                     float(stock["profit"])
                                     ))

        portfolio = self.optimized_portfolio(stocks_list)
        # portfolio = self.bruteforce_portfolio(stocks_list)

        self.view.stocks_to_buy_with_gain(portfolio)
        print("--- %s s ---" % ((time.time()*1000) - start_time))
