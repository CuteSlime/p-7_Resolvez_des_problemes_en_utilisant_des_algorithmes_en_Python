from Models.stock import Stock
from Models.portfolio import Portfolio


stocks = [
    {"name": "Action-1", "stock_price": 20, "percent_gain": 5},
    {"name": "Action-2", "stock_price": 30, "percent_gain": 10},
    {"name": "Action-3", "stock_price": 50, "percent_gain": 15},
    {"name": "Action-4", "stock_price": 70, "percent_gain": 20},
    {"name": "Action-5", "stock_price": 60, "percent_gain": 17},
    {"name": "Action-6", "stock_price": 80, "percent_gain": 25},
    {"name": "Action-7", "stock_price": 22, "percent_gain": 7},
    {"name": "Action-8", "stock_price": 26, "percent_gain": 11},
    {"name": "Action-9", "stock_price": 48, "percent_gain": 13},
    {"name": "Action-10", "stock_price": 34, "percent_gain": 27},
    {"name": "Action-11", "stock_price": 42, "percent_gain": 17},
    {"name": "Action-12", "stock_price": 110, "percent_gain": 9},
    {"name": "Action-13", "stock_price": 38, "percent_gain": 23},
    {"name": "Action-14", "stock_price": 14, "percent_gain": 1},
    {"name": "Action-15", "stock_price": 18, "percent_gain": 3},
    {"name": "Action-16", "stock_price": 8, "percent_gain": 8},
    {"name": "Action-17", "stock_price": 4, "percent_gain": 12},
    {"name": "Action-18", "stock_price": 10, "percent_gain": 14},
    {"name": "Action-19", "stock_price": 24, "percent_gain": 21},
    {"name": "Action-20", "stock_price": 114, "percent_gain": 18},
]


def optimized_portfolio(stocks_list):
    sorted_stocks = sorted(stocks_list,
                           key=lambda stock: stock.gain,
                           reverse=True
                           )
    portfolio = Portfolio()

    for stock in sorted_stocks:
        if stock.stock_price <= portfolio.investment:
            portfolio.add_stock(stock)
            portfolio.investment -= stock.stock_price

    return portfolio


class Controller():
    def __init__(self, view):
        self.view = view

    def run(self):
        stocks_list = []
        for stock in stocks:
            stocks_list.append(Stock(stock["name"],
                                     stock["stock_price"],
                                     stock["percent_gain"]
                                     ))

        portfolio = optimized_portfolio(stocks_list)

        self.view.stocks_to_buy_with_gain(portfolio)
