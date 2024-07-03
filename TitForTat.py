class TitForTat:

    def strategy(self, opponent: bool):
        if opponent:
            return True
        return False


class ForgivingTitForTat:

    def __init__(self):
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
