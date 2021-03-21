import utils
import json

playerOneTeam = []
playerTwoTeam = []

def build(numberOfCharacters, player, playerName):
    count = 0
    while count < numberOfCharacters :
        utils.clearScreen()
        count += 1
        ordinal = None
        if (count == 1):
            ordinal = 'first'
        elif (count == 2):
            ordinal = 'second'
        elif (count == 3):
            ordinal = 'third'
        elif (count == 4):
            ordinal = 'fourth'
        elif (count == 5):
            ordinal = 'fifth'
        print("Nice to meet you " + playerName + ", let's build your team!\n")
        print("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defense\n[M]age - A spell caster with low attack and defense\n""")
        characterClassInput = str(input("Pick a class for your " + ordinal + " character: "))
        characterNameInput = str(input("What is your character's name?: "))
        playerUnits = {"character_class": characterClassInput.upper(), "character_name": characterNameInput}
        if (player == 1):
            playerOneTeam.append(playerUnits)
        elif (player == 2):
            playerTwoTeam.append(playerUnits)

    if (player == 1):
        return playerOneTeam
    elif (player == 2):
        return playerTwoTeam

def save(characters, player, playerName):
    for character in characters:
        if (character["character_class"]) == "T":
            trollFile = open("init/troll.json", "r")
            trollJson = trollFile.read()
            troll = json.loads(trollJson)
            troll["name"] = character["character_name"]
            gameFile = open("game.json","r")
            gameJson = gameFile.read()
            game = json.loads(gameJson)
            if (player == 1):
                game["player_one"]["name"] = playerName
                game["player_one"]["team"].append(troll)
            elif (player == 2):
                game["player_two"]["name"] = playerName
                game["player_two"]["team"].append(troll)
            with open('game.json','w') as outfile:
                json.dump(game, outfile)
        elif (character["character_class"]) == "K":
            knightFile = open("init/knight.json", "r")
            knightJson = knightFile.read()
            knight = json.loads(knightJson)
            knight["name"] = character["character_name"]
            gameFile = open("game.json","r")
            gameJson = gameFile.read()
            game = json.loads(gameJson)
            if (player == 1):
                game["player_one"]["name"] = playerName
                game["player_one"]["team"].append(knight)
            elif (player == 2):
                game["player_two"]["name"] = playerName
                game["player_two"]["team"].append(knight)
            with open('game.json','w') as outfile:
                json.dump(game, outfile)
        elif (character["character_class"]) == "M":
            mageFile = open("init/mage.json", "r")
            mageJson = mageFile.read()
            mage = json.loads(mageJson)
            mage["name"] = character["character_name"]
            gameFile = open("game.json", "r")
            gameJson = gameFile.read()
            game = json.loads(gameJson)
            if (player == 1):
                game["player_one"]["name"] = playerName
                game["player_one"]["team"].append(mage)
            elif (player == 2):
                game["player_two"]["name"] = playerName
                game["player_two"]["team"].append(mage)
            with open('game.json', 'w') as outfile:
                json.dump(game, outfile)