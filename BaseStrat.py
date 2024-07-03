class Strategy:

    def __init__(self, name):
        self.name = name
        self.points = 0

    ## will be changed for each child class of strategy
    def strategy(self):
        return True

