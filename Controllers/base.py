# import itertools
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


def sort_stocks(stocks_list: list):
    '''Trie la liste des actions par gain

    Args:
        stocks_list (_list_): liste des actions à trier

    Returns:
        _list_: liste des actions trier par gain
    '''

    i = 0
    sorted_stocks = []
    not_sorted_stocks = stocks_list[:]
    while i < len(stocks_list):
        gain = 0

        best_stock = not_sorted_stocks[0]
        for stock in not_sorted_stocks:
            if stock.gain > gain:
                gain = stock.gain
                best_stock = stock
        sorted_stocks.append(best_stock)
        not_sorted_stocks.remove(best_stock)
        i += 1
    return sorted_stocks


class Controller():
    def __init__(self, view):
        self.view = view

    def run(self):
        stocks_list = []
        # portfolio_list = []
        for stock in stocks:
            stocks_list.append(
                Stock(stock["name"], stock["stock_price"], stock["percent_gain"]))
# sort_stocks(stocks_list)
        sorted_stocks = sorted(
            stocks_list, key=lambda stock: stock.gain, reverse=True)
        portfolio = Portfolio()

        for stock in sorted_stocks:
            if stock.stock_price <= portfolio.investment:
                portfolio.add_stock(stock)
                portfolio.investment -= stock.stock_price

        for stock in portfolio.stock_list:
            print(stock.name)
        print("Total Gain:", portfolio.calculate_total_gain())
        # stocks_number = len(stocks_list)
        # for stock in stocks_list:
        #     i=0
        #     while i <= stocks_number:
        #         portfolio_list.append(Portfolio(stock_list=stock))
        #         i+= 1

        # new_stocks_list = stocks_list[:]

    # def compatible_stocks(list_action, portfolio_list):
    #     for portfolio in portfolio_list:
    #     if list_action == []:
    #         return
    #     edited_list_action = list_action[:]
    #     action_possible = []
    #     for action in edited_list_action:
    #         if (rest - action) >= 0:
    #             action_possible.append(action)
    #     return compatible_stocks(rest, action_possible)


# fonction(list d'action)
# action_possible = list_action[:]
# dans la list d'action on teste
# action[i] + chaque action
# si : l'action dépasse la limite on l'ajoute au [action inpossible]
# si : l'action ne dépasse pas la limite on l'ajoute au [action possible] index
# on fait list [best action]

# on refait une boucle sur la list des [action possible] en enlevant action[i] de l'inverstissement possible


#  invest_list = []
#         while len(new_stocks_list) > 0:
#             # print(new_stocks_list)
#             investment = 500
#             new_stocks_list = new_stocks_list[:]
#             temp_stocks_list = []
#             for stock in new_stocks_list:
#                 if stock.stock_price < investment:
#                     investment -= stock.stock_price
#                     temp_stocks_list.append(stock)
#                     # print(
#                     #     f"{stock.name} après investisement laisse {investment} à utilisé")
#             invest_list.append(temp_stocks_list)
#             # print(temp_stocks_list)

#             del new_stocks_list[0]
#         print(invest_list)
#         for i, stock in enumerate(new_stocks_list):
#             investment = 500
#             if i in invest_list.items():

#             invest_list
#             print(stock, i)
