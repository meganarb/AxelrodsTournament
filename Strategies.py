class Strategy:

    def __init__(self, name):
        self.name = name
        self.points = 0

    # will be changed for each child class of strategy
    def strategy(self, opponent:bool):
        return True


class TitForTat(Strategy):

    def strategy(self, opponent:bool):
        if opponent:
            return True
        return False


class TitForTwoTats(Strategy):

    def __init__(self, name):
        Strategy.__init__(self, name)
        self.betray = False

    def strategy(self, opponent: bool):
        if opponent:
            self.betray = False
            return True
        elif not opponent:
            if self.betray:
                return False
            self.betray = True
            return True
