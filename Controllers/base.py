# import itertools
from Models.share import Share
shares = [
    {"name": "Action-1", "share_price": 20, "percent_gain": 5},
    {"name": "Action-2", "share_price": 30, "percent_gain": 10},
    {"name": "Action-3", "share_price": 50, "percent_gain": 15},
    {"name": "Action-4", "share_price": 70, "percent_gain": 20},
    {"name": "Action-5", "share_price": 60, "percent_gain": 17},
    {"name": "Action-6", "share_price": 80, "percent_gain": 25},
    {"name": "Action-7", "share_price": 22, "percent_gain": 7},
    {"name": "Action-8", "share_price": 26, "percent_gain": 11},
    {"name": "Action-9", "share_price": 48, "percent_gain": 13},
    {"name": "Action-10", "share_price": 34, "percent_gain": 27},
    {"name": "Action-11", "share_price": 42, "percent_gain": 17},
    {"name": "Action-12", "share_price": 110, "percent_gain": 9},
    {"name": "Action-13", "share_price": 38, "percent_gain": 23},
    {"name": "Action-14", "share_price": 14, "percent_gain": 1},
    {"name": "Action-15", "share_price": 18, "percent_gain": 3},
    {"name": "Action-16", "share_price": 8, "percent_gain": 8},
    {"name": "Action-17", "share_price": 4, "percent_gain": 12},
    {"name": "Action-18", "share_price": 10, "percent_gain": 14},
    {"name": "Action-19", "share_price": 24, "percent_gain": 21},
    {"name": "Action-20", "share_price": 114, "percent_gain": 18},
    ]


class Controller():
    def __init__(self, view):
        self.view = view

    def run(self):
        shares_list = []
        for share in shares:
            shares_list.append(Share(share["name"], share["share_price"], share["percent_gain"]))
        print(shares_list[1].__dict__)
        for share in shares_list:
            new_shares_list = shares_list[:]
            investment = 500 - share.share_price
            print(f"{share.name} après investisement laisse {investment} à utilisé")
            new_shares_list.remove(share)
            # for share in new_shares_list:
            # while investment > min([share_price['share_price'] for share_price in new_shares_list]):
