class Strategy:

    def __init__(self, name):
        self.name = name
        self.points = 0

    # will be changed for each child class of strategy, the base class always cooperates
    def strategy(self, opponent: bool):
        return True


class TitForTat(Strategy):  # always cooperates, only defects after opponent defects

    def strategy(self, opponent: bool):
        if opponent:
            return True
        return False


class TitForTwoTats(Strategy):  # always cooperates, only defects after opponent defects twice in a row

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


class AlwaysDefects(Strategy):  # aptly named

    def strategy(self, opponent: bool):
        return False


class NoForgiveness(Strategy):  # always cooperates until opponent defects; then always defects

    def __init__(self, name):
        Strategy.__init__(self, name)
        self.cooperate = True

    def strategy(self, opponent: bool):
        if not opponent:
            self.cooperate = False
        return self.cooperate


class TwoTitsForTat(Strategy):  # always cooperates until opponent defects, and then defects twice

    def __init__(self, name):
        Strategy.__init__(self, name)
        self.repeat = False

    def strategy(self, opponent: bool):
        if opponent:
            if self.repeat:
                self.repeat = False
                return False
            return True
        self.repeat = True
        return False
