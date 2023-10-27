
class View():
    def __init__(self):
        pass

    def stocks_to_buy_with_gain(self, portfolio):
        for stock in portfolio.stock_list:
            print(f"{stock.name} raporte : {stock.gain}€")
        print(f"montant total des actions :{500 - portfolio.investment}€")
        print("Gain total des actions apres 2 ans :",
              round(portfolio.calculate_total_gain(), 2), "€")
