# Maria Dimitropoulou, A.M. 4664
import random
from random import randint

# Input
players = int(input("Number of players: "))
beans = int(input("Number of beans per player: "))

# Lists and variables
lst = ["put 1", "put 2", "put all", "take 1", "take 2", "take all"]
y = randint(1, players)  # random player
lstb = [beans] * players  # beans per player
lst2 = [beans] * players  # copy for elimination check
print("The first player is Player", y)
e = 1  # rounds
r = 0  # eliminated count
players_on = players

# Game loop
while r < players - 1:
    print("-" * 35)
    print("Round", e, " begins: everyone puts 1")
    
    # Everyone puts 1 if possible
    for b in range(players):
        if lstb[b] > 0:
            lstb[b] -= 1
        else:
            lst2[b] = "eliminated"
    
    # Count eliminated and active players
    r = lst2.count("eliminated")
    players_on = players - r
    pot = players_on  # pot after everyone puts 1
    
    print("Current state:")
    print("Pot:", pot)
    for n in range(players):
        if lst2[n] == "eliminated":
            print("Player", n + 1, "is eliminated")
        else:
            print("Player", n + 1, "budget:", lstb[n])
    
    # Winner check
    if r >= players - 1:
        break
    
    # Spin until pot = 0
    while pot > 0:
        # Skip eliminated players
        if lst2[y - 1] == "eliminated":
            y = (y % players) + 1
            continue
        
        w = random.choice(lst)
        print("\nPlayer", y, "spinned", w)
        
        # Actions
        if w == "put 1":
            if lstb[y - 1] > 0:
                lstb[y - 1] -= 1
                pot += 1
        
        elif w == "put 2":
            if lstb[y - 1] >= 2:
                lstb[y - 1] -= 2
                pot += 2
            elif lstb[y - 1] == 1:
                lstb[y - 1] -= 1
                pot += 1
        
        elif w == "put all":  # Everyone puts 1 if possible
            for x in range(players):
                if lstb[x] > 0 and lst2[x] != "eliminated":
                    lstb[x] -= 1
                    pot += 1
        
        elif w == "take 1":
            if pot >= 1:
                pot -= 1
                lstb[y - 1] += 1
        
        elif w == "take 2":
            if pot >= 2:
                pot -= 2
                lstb[y - 1] += 2
            elif pot == 1:
                pot -= 1
                lstb[y - 1] += 1
        
        elif w == "take all":
            lstb[y - 1] += pot
            pot = 0
        
        # Update eliminated players
        for i in range(players):
            if lstb[i] <= 0:
                lst2[i] = "eliminated"
        
        # Print state
        print("Current state:")
        print("Pot:", pot)
        for n in range(players):
            if lst2[n] == "eliminated":
                print("Player", n + 1, "is eliminated")
            else:
                print("Player", n + 1, "budget:", lstb[n])
        
        # If pot is empty, end round
        if pot == 0:
            print("\nPot is zero: round ends")
            break
        
        # Next player's turn
        y = (y % players) + 1
        
        # Check if only one remains
        r = lst2.count("eliminated")
        if r >= players - 1:
            break
    
    e += 1

# Final result
winners = [i + 1 for i in range(players) if lst2[i] != "eliminated"]
if len(winners) == 1:
    print("\nWinner is Player", winners[0])
else:
    print("\nIt's a tie")