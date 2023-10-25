from Controllers.base import Controller


class View():
    def __init__(self):
        pass

    def stocks_to_buy_with_gain(self, portfolio):
        for stock in portfolio.stock_list:
            print(f"{stock.name} raporte : {stock.gain}")
        print(f"{portfolio.investment} restant sur le compte")
        print("Total Gain:", portfolio.calculate_total_gain())
