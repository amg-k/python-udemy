import random
import enum
import time

def idle(sec, reps):
    for i in range(reps):
        print(".")
        time.sleep(sec)

def chest_loot(chest):
    if chest == ChestTypes.Green:
        return ChestLootDictGen[ChestTypes.Green]
    elif chest == ChestTypes.Orange:
        return ChestLootDictGen[ChestTypes.Orange]
    elif chest == ChestTypes.Purple:
        return ChestLootDictGen[ChestTypes.Purple]
    elif chest == ChestTypes.Gold:
        return ChestLootDictGen[ChestTypes.Gold]

def aproximate_num(num, margin):
    lowValue = num * (1 - margin)
    highValue = num * (1 + margin)
    return random.randint(lowValue, highValue)

gameLength = 5
score = 0

EventsTypes = enum.Enum('Events_Types',
                        ['Chest',
                         'Nothing'])
EventsDictionary = {EventsTypes.Chest: 0.6,
                    EventsTypes.Nothing: 0.4}              
EventsList = list(EventsDictionary.keys())
EventsProbability = list(EventsDictionary.values())

ChestTypes = enum.Enum('Chest_Types',
                       ['Green',
                        'Orange',
                        'Purple',
                        'Gold'])
ChestProbDict = {ChestTypes.Green: 0.75,
                   ChestTypes.Orange: 0.2,
                   ChestTypes.Purple: 0.04,
                   ChestTypes.Gold: 0.01}

ChestList = list(ChestProbDict.keys())
ChestProbability = list(ChestProbDict.values())

ChestLootDictGen = {ChestList[rep]: (rep + 1)**2 * 1000 
                    for rep in range(len(ChestList))
                    }

print("""In this game you are crossing a chamber
where is a chance of finding a chest full of gold.
Let's check what you've got! \n""")


while gameLength > 0:
    gamerMove = input("Focus and type 'yes' to move forward \n")
    if gamerMove == "yes":
        print("Prepare yourself!! In a while your destiny will occur!")
        chosenEvent = random.choices(EventsList, EventsProbability)[0]    #wybrać "0" element z jednoelementowej listy!!
        if chosenEvent == EventsTypes.Chest:
            chosenChest = random.choices(ChestList, ChestProbability)[0]
            print("Congratulations!! You've found a treasure chest!!")
            print("Let's see how many gold is inside... Opening...")
            idle(0.3, 3)
            playerLoot = aproximate_num(chest_loot(chosenChest), 0.1)
            print("You've found", playerLoot, "of gold !!")
            score += playerLoot
            print("Your current score is:", score)
        elif chosenEvent == EventsTypes.Nothing:
            print("Nothing found... Try again")
    else:
        print("Move failed, try again!")
        continue
    gameLength -= 1
    
print("\nYou succesfully leave the Chamber! Your final score is:", score)
