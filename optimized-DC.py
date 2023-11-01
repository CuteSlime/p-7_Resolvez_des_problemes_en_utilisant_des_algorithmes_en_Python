import time
import csv


start_time = time.time() * 1000


class Stock():
    def __init__(self, name, price, percent_gain):
        self.name = name
        self.price = int(price * 100)
        self.percent_gain = int(percent_gain*100)
        self.gain = (price * percent_gain) / 100


class Portfolio():
    def __init__(self, **kwargs):
        self.stock_list = kwargs.get("stock_list", [])
        self.investment = int(kwargs.get("investment", 500)*100)

    def add_stock(self, stock: object):
        self.stock_list.append(stock)
        self.investment -= stock.price

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


def generate_matrice(stocks, max_investment):
    '''construction de la matrice de programation dynamique

    Args:
        stocks (_list_): liste d'objet Stock du quelle on utilise le gain et le price
        max_investment (_int_): le price maximum tirer de l'objet Portofolio
    '''

    nb_stocks = len(stocks)
    matrice = [[0 for investment in range(max_investment+1)]
               for stock in range(nb_stocks+1)]
    for stock in range(1, nb_stocks+1):
        # stock = int(stock)
        index = stock-1
        for investment in range(max_investment+1):
            if investment >= stocks[index].price:

                matrice[stock][investment] = max(matrice[stock-1][investment], stocks[index].gain +
                                                 matrice[stock-1][investment-(stocks[index].price)])
            else:
                matrice[stock][investment] = matrice[stock-1][investment]
    return matrice


def stock_to_buy(nb_stocks, max_investment, stocks, matrice):

    if nb_stocks == 0:
        return []
    if matrice[nb_stocks][max_investment] > matrice[nb_stocks - 1][max_investment]:
        return [stocks[nb_stocks - 1]] + stock_to_buy(nb_stocks - 1,
                                                      max_investment -
                                                      stocks[nb_stocks -
                                                             1].price,
                                                      stocks,
                                                      matrice
                                                      )
    else:
        return stock_to_buy(nb_stocks - 1, max_investment, stocks, matrice)


def optimized_portfolio(stocks_list):
    portfolio = Portfolio()
    matrice = generate_matrice(stocks_list, portfolio.investment)
    portfolio.stock_list = stock_to_buy(
        len(stocks_list), portfolio.investment, stocks_list, matrice)

    portfolio.investment /= 100

    for stock in portfolio.stock_list:
        stock.price /= 100
        stock.percent_gain /= 100
        portfolio.investment -= stock.price
    return portfolio


filename = 'dataset2_Python+P7'
stocks = csv_converter(filename)
stocks_list = [Stock(stock["name"], float(stock["price"]),
                     float(stock["profit"])) for stock in stocks]


portfolio = optimized_portfolio(stocks_list)

for stock in portfolio.stock_list:
    print(f"{stock.name} raporte : {round(stock.gain, 2)}€")
print(f"montant total des actions :{round((500 - portfolio.investment), 2)}€")
print("Gain total des actions apres 2 ans :",
      round(portfolio.calculate_total_gain(), 2), "€"
      )
print("--- %s ms ---" % ((time.time()*1000) - start_time))
