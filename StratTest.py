import Strategies


def PlayerIter(rounds: int, players: Strategies):  # iterates through all combinations of players

    for i in range(len(players) - 1):
        for j in range(i + 1, len(players)):
            temp(rounds, players[i], players[j])
    return players  # other methods will have changed their scores


def StrategyTest(rounds: int, player1, player2):

    past1 = True
    past2 = True
    p1Choice: bool
    p2Choice: bool

    for i in range(rounds):
        p1Choice = player1.strategy(past1)
        p2Choice = player2.strategy(past2)

        if p1Choice and p2Choice:
            player1.points += 3
            player2.points += 3

        elif p1Choice and not p2Choice:
            player2.points += 5

        elif p2Choice and not p1Choice:
            player1.points += 5

        else:
            player1.points += 1
            player2.points += 1

        past1 = p1Choice
        past2 = p2Choice

    # puts players against each other for x rounds


p1 = Strategies.TitForTat("p1")
p2 = Strategies.TitForTwoTats("p2")
p3 = Strategies.Strategy("p3")
Test(5, [p1, p2, p3])

print(p1.points)
print(p2.points)
print(p3.points)