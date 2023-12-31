import time

# chrono
start_time = time.time() * 1000
MAX_INVESTMENT = 500
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


class Stock():
    def __init__(self, name, stock_price, percent_gain):
        self.name = name
        self.stock_price = stock_price
        self.percent_gain = percent_gain
        self.gain = (stock_price * percent_gain) / 100


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


def create_portfolio(list_tulpes_stocks):
    '''iter on a list of tulpe to get the best portofolio,

    Args:
        list_tulpes_stocks (list): a list of tulpe where each tulpe contain a list of stocks

    Returns:
        object: return the best portofolio of stocks
    '''

    max_total_gain = 0
    best_portfolio = ""

    for list_of_stocks in list_tulpes_stocks:
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


def bruteforce_portfolio(stocks_list: list):
    '''use combinations to make a list (list_tulpes_stocks) of all posibility,
       and call create_portfolio with it to get the best portofolio.


    Args:
        stocks_list (list): list of all stocks

    Returns:
        object: return an object portofolio
    '''

    i = 2
    list_tulpes_stocks = []
    while i <= len(stocks_list):
        list_of_tulpes = ()
        list_of_tulpes = combinations(stocks_list, i, MAX_INVESTMENT)
        list_tulpes_stocks.extend(list_of_tulpes)
        i += 1
    portfolio = create_portfolio(list_tulpes_stocks)

    return portfolio


def combinations(iterable, group_by, investment):
    '''divide a list into group and return the best ones

    Args:
        iterable (list): a list of objects
        group_by (int): the number of object to take from the list to add into group
        investment (int): the amount of max investment

    Yields:
        list: a list of tulpes
    '''

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


# main code
stocks_list = []

for stock in stocks:
    stocks_list.append(Stock(stock["name"],
                             float(stock["price"]),
                             float(stock["profit"])
                             ))


portfolio = bruteforce_portfolio(stocks_list)

for stock in portfolio.stock_list:
    print(f"{stock.name} coût: { round(stock.stock_price, 2)} gain :{ round(stock.gain, 2)}€")
print(f"coût total :{round(500 - portfolio.investment, 2)}€")
print("Gain total :",
      round(portfolio.calculate_total_gain(), 2), "€")
print("--- %s ms ---" % ((time.time()*1000) - start_time))
