class Share():
    def __init__(self, name, share_price, percent_gain):
        self.name = name
        self.share_price = share_price
        self.percent_gain = percent_gain
        self.gain = (share_price * percent_gain) / 100
