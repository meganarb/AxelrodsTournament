import Strategies


def Test(rounds: int, players: Strategies):  # iterates through all combinations of players

    for i in range(len(players) - 1):
        for j in range(i + 1, len(players)):
            temp(rounds, players[i], players[j])
    return players  # other methods will have changed their scores


def temp(rounds: int, player1, player2):

    zero = 0
    # puts players against each other for x rounds
def FaceOff(strat1, strat2):

    zero = 0
    # testing two individual strats against one another
    # returns the winning strat


p1 = Strategies.TitForTat("p1")
p2 = Strategies.TitForTwoTats("p2")
Test(0, [p1, p2, p1, p1, p1, p1])