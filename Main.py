import random
Board = ['Go','Tin Shui Wai','Community Chest 1','Cheung Chau','Income Tax','Tung Chung Station','Ap Lei Chau','Chance 1','Kwun Tong','Lam Tin',"Jail","Tuen Mun","Hong Kong Electric","Yuen Long","Tai Po","Tsing Yi Station","Tai Wai","Community Chest 2","Sha Tin","Ma On Shan","Free Parking","Tseung Kwan O","Chance 2","Tsuen Wan","Aberdeen","Kowloon Tong Station","Mong Kok","Tsim Sha Tsui","Water Works","West Kowloon","Go to Jail","Causeway bay","Wan Chai","Community Chest 3","Central","Hong Kong Station","Chance 3","Pok Fu Lam","Super Tax","The Peak"]
Movement = ['Go']
PlayerPos = ['Go']

def roll(PlayerPos):
    Dice1RollValue = random.randint(1,6)
    Dice2RollValue = random.randint(1,6)
    SumRollValue = Dice1RollValue+Dice2RollValue

    #Adding the roll to the player pos, accounting for instances where the array index is out of bounds
    UpdatedPos = (Board.index(PlayerPos[-1]) + SumRollValue) % len(Board)
    PlayerPos.append(Board[UpdatedPos])

    row = [SumRollValue]
    Movement.append(row)

for x in range(10):
    roll(PlayerPos)

for x in range(len(Movement)):
    print(Movement[x],PlayerPos[x])
