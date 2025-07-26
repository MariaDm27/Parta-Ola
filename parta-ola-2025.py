import random

def print_state(pot, players):
    print(f"Pot: {pot}")
    for i, beans in enumerate(players, start=1):
        status = f"budget: {beans}" if beans >= 0 else "is eliminated"
        print(f"Player {i} {status}")
    print()

def play_turn(player, action, pot, players):
    if players[player] < 0:
        return pot  # skip eliminated

    if action == "put 1":
        if players[player] > 0:
            players[player] -= 1
            pot += 1
    elif action == "put 2":
        amount = min(2, players[player])
        players[player] -= amount
        pot += amount
    elif action == "put all":
        for i in range(len(players)):
            if players[i] > 0:
                players[i] -= 1
                pot += 1
    elif action == "take 1":
        if pot > 0:
            players[player] += 1
            pot -= 1
    elif action == "take 2":
        take = min(2, pot)
        players[player] += take
        pot -= take
    elif action == "take all":
        players[player] += pot
        pot = 0

    return pot

def main():
    n = int(input("Number of players: "))
    beans = int(input("Number of beans per player: "))
    players = [beans] * n
    actions = ["put 1", "put 2", "put all", "take 1", "take 2", "take all"]
    pot, round_num, current = 0, 1, random.randint(0, n - 1)

    print(f"The first player is Player {current + 1}\n")

    while sum(p >= 0 for p in players) > 1:
        print("-" * 40)
        print(f"Round {round_num} begins: everyone puts 1")
        pot = 0
        for i in range(n):
            if players[i] > 0:
                players[i] -= 1
                pot += 1
            else:
                players[i] = -1
        print_state(pot, players)

        while pot > 0 and sum(p >= 0 for p in players) > 1:
            action = random.choice(actions)
            print(f"Player {current + 1} spinned {action}")
            pot = play_turn(current, action, pot, players)
            print_state(pot, players)
            if pot == 0:
                print("Pot is zero: round ends\n")
            current = (current + 1) % n

        round_num += 1

    winner = [i + 1 for i, p in enumerate(players) if p >= 0]
    if len(winner) == 1:
        print(f"Game finished: Player {winner[0]} wins")
    else:
        print("Game finished: It's a tie")

if __name__ == "__main__":
    main()
