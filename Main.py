import random
Board = ['Go','Tin Shui Wai','Community Chest 1','Cheung Chau','Income Tax','Tung Chung Station','Ap Lei Chau','Chance 1','Kwun Tong','Lam Tin',"Jail","Tuen Mun","Hong Kong Electric","Yuen Long","Tai Po","Tsing Yi Station","Tai Wai","Community Chest 2","Sha Tin","Ma On Shan","Free Parking","Tseung Kwan O","Chance 2","Tsuen Wan","Aberdeen","Kowloon Tong Station","Mong Kok","Tsim Sha Tsui","Water Works","West Kowloon","Go to Jail","Causeway bay","Wan Chai","Community Chest 3","Central","Hong Kong Station","Chance 3","Pok Fu Lam","Super Tax","The Peak"]
Movement = [['Go'],['Go'],['Go'],['Go']]
PlayerPos = [['Go'],['Go'],['Go'],['Go']]
Players = 0

def roll(Players):
    Dice1RollValue = random.randint(1,6)
    Dice2RollValue = random.randint(1,6)
    SumRollValue = Dice1RollValue+Dice2RollValue

    #Adding the roll to the player pos, accounting for instances where the array index is out of bounds
    UpdatedPos = (Board.index(PlayerPos[Players][-1]) + SumRollValue) % len(Board)
    PlayerPos[Players].append(Board[UpdatedPos])

    Movement[Players].append(SumRollValue)

for x in range(10):
    roll(Players=0)
    roll(Players=1)
    roll(Players=2)
    roll(Players=3)

for x in range(10):
    print(Movement[0][x],PlayerPos[0][x])
print("Player 1 done")

for x in range(10):
    print(Movement[1][x],PlayerPos[1][x])
print("Player 2 done")

for x in range(10):
    print(Movement[2][x],PlayerPos[2][x])
print("Player 3 done")

for x in range(10):
    print(Movement[3][x],PlayerPos[3][x])
print("Player 4 done")
