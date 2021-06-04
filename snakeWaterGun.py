import random
l = ['snake', 'water', 'gun']
win = 0
loose = 0
rounds = 0
while(rounds < 10):
    r = random.choice(l)
    ch = input("S for Snake\nW for Water\nG for Gun\nEnter you choice: ")
    if((ch == 's' and r == 'snake') or (ch == 'w' and r == 'water') or (ch == 'g' and r == 'gun')):
        print("Match Draw in this Round!")
    elif((ch == 's' and r == 'water') or (ch == 'w' and r == 'gun') or (ch == 'g' and r == 'snake')):
        print("You Won in this Round!")
        win += 1
    elif((ch == 's' and r == 'gun') or (ch == 'w' and r == 'snake') or (ch == 'g' and r == 'water')):
        print("You Loose in this Round!")
        loose += 1
    rounds += 1
    print("Rounds Played:", rounds)

if win > 5:
    print("\nYou won the game")
    print(f"And won {win} rounds.")
elif win == 5:
    print("\nMatch Draw")
    print(f"You won {win} rounds.")
else:
    print("\nYou lost the game :(")
    print(f"And won only {win} rounds.")
