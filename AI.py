#UI/UX
import json


#Lists used in the game
playerOneListOfUnits = []
playerTwoListOfUnits = []
playerOne = []
playerTwo = []
AIListOfUnits=[]
AIclass=[]
FirstName=["Jay " , "Luis " , "Bob " , "Sofi ", "Susan "]
LastName=['Smith','Hughes','Evans','Hemsworth','Odinson']

#######END OF LIST#######


#Functions used in the game




#For List of Units of playerOne
def playerOneCharacters (playerOneNumberOfUnits):
    count = 0
    while count < playerOneNumberOfUnits :
        print(count + 1)
        print ("Choose a character for your team")
        print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
        characterClassInput = str(input("Enter chosen character:"))
        
        while True:
            if characterClassInput.lower() =='k':
                print ("You have chosen Knight")
                break
            elif characterClassInput.lower() =='t':
                print ("You have chosen Troll")
                break
            elif characterClassInput.lower() =='m':
                print ('You have chosen Mage')
                break
            else:
                print ('Invalid input. Please try again!')
                characterClassInput = str(input("Enter chosen character:"))
                continue
                
        else:
            print ('Invalid input. Please try again!')
            break
        characterNameInput = str(input("Enter character's name:"))
        while True:
            if characterNameInput == '':
                print ('You have not enter a name. Please try again!')
                characterNameInput = str(input("Enter character's name:"))
            else:
                break

            
        
        localplayerOneListOfUnits = {"character_class":characterClassInput, "character_name":characterNameInput}
        playerOneListOfUnits.append(localplayerOneListOfUnits)
        count = count + 1

#For List of Units of playerTwo
def playerTwoCharacters (playerTwoNumberOfUnits):
    count = 0
    while count < playerTwoNumberOfUnits :
        print(count + 1)
        print ("Choose a character for your team")
        print ("""[T]roll - A strong attack but careless monster that has 50% chance of missing its target\n[K]night - A soldier with decent attack and strong defence\n[M]age - A spell caster with low attack/defence""")
        characterClassInput = str(input("Enter chosen character:"))
        while True:
            if characterClassInput.lower() =='k':
                print ("You have chosen Knight")
                break
            elif characterClassInput.lower() =='t':
                print ("You have chosen Troll")
                break
            elif characterClassInput.lower() =='m':
                print ('You have chosen Mage')
                break
            else:
                print ('Invalid input. Please try again!')
                characterClassInput = str(input("Enter chosen character:"))
                
                continue
        characterNameInput = str(input("Enter character's name:"))
        while True:
            if characterNameInput == '':
                print ('You have not enter a name. Please try again!')
                characterNameInput = str(input("Enter character's name:"))
            else:
                break
        localplayerTwoListOfUnits = {"character_class":characterClassInput, "character_name":characterNameInput}
        playerTwoListOfUnits.append(localplayerTwoListOfUnits)
        count = count + 1

#To config units to JSON
def configOneUnits(playerOneListOfUnits):
    for unit in playerOneListOfUnits:
        if (unit["character_class"]) == "T":
            trollFile = open("init/troll.json", "r")
            trollJson = trollFile.read()
            troll = json.loads(trollJson)
            troll["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(troll)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "K":
            knightFile = open("init/knight.json", "r")
            knightJson = knightFile.read()
            knight = json.loads(knightJson)
            knight["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(knight)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "M":
            mageFile = open("init/mage.json", "r")
            mageJson = mageFile.read()
            mage = json.loads(mageJson)
            mage["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(mage)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)

def configTwoUnits(playerTwoListOfUnits):
    for unit in playerOneListOfUnits:
        if (unit["character_class"]) == "T":
            trollFile = open("init/troll.json", "r")
            trollJson = trollFile.read()
            troll = json.loads(trollJson)
            troll["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_two"]["team"].append(troll)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "K":
            knightFile = open("init/knight.json", "r")
            knightJson = knightFile.read()
            knight = json.loads(knightJson)
            knight["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_two"]["team"].append(knight)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "M":
            mageFile = open("init/mage.json", "r")
            mageJson = mageFile.read()
            mage = json.loads(mageJson)
            mage["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_two"]["team"].append(mage)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)

#AI Team
def generateRandomPlayers(playerOneNumberOfUnits):
    import random
    unitlist=['Troll', 'Knight', 'Mage']
    for unit in range(1,playerOneNumberOfUnits+1):
        AIunit=random.choice(unitlist)
        print (AIunit)
        if AIunit=='Troll':
            AIunit='T'
        elif AIunit=='Knight':
            AIunit='K'
        elif AIunit=='Mage':
            AIunit='M'
        AIListOfUnits.append(AIunit)
    AInumberOfUnits=len(AIListOfUnits)
    count = 0
    for count in range(0,AInumberOfUnits) :
        characterClassInput = AIListOfUnits[count]
        characterNameInput = str(random.choice(FirstName))+str(random.choice(LastName))
        localAIListOfUnits = {"character_class":characterClassInput, "character_name":characterNameInput}
        AIclass.append(localAIListOfUnits)
    print (AIclass)

def configAIUnits(AIclass):
    for unit in AIclass:
        if (unit["character_class"]) == "T":
            trollFile = open("init/troll.json", "r")
            trollJson = trollFile.read()
            troll = json.loads(trollJson)
            troll["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(troll)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "K":
            knightFile = open("init/knight.json", "r")
            knightJson = knightFile.read()
            knight = json.loads(knightJson)
            knight["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(knight)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)
        elif (unit["character_class"]) == "M":
            mageFile = open("init/mage.json", "r")
            mageJson = mageFile.read()
            mage = json.loads(mageJson)
            mage["name"] = unit["character_name"]
            configFile = open("config.json","r")
            configJson = configFile.read()
            config = json.loads(configJson)
            config["player_one"]["team"].append(mage)
            with open('config.json','w') as outfile:
                json.dump(config, outfile)


#######END OF FUNCTIONS#######



#INTRODUCE PSB BATTLE GAME TO USER

print ("WELCOME TO PSB BATTLE GAME")
str(input("Press enter to proceed"))

#MENU OPTIONS
Menu=("Menu \n[N]ew Game \n[R]esume Game \n[H]ow to Play \n[E]xit Game")
print (Menu)

#USER TO KEY IN CHOSEN MENU
while True:
    chosenMenu = str(input("Choose menu option: "))
    #New Game
    if chosenMenu.lower() == 'n': 
        print ("Choose your game mode:")
        print ("[1] Player vs AI")
        print ("[2] Player vs Player")
        #Game Mode
        gameMode = int(input("Game mode chosen:"))
        while True:
            try:
                if gameMode==1: #Player VS AI
                    #PLAYER 1
                    playerOneName = str(input("Player 1's name:"))
                    while True:
                        if playerOneName == '':
                            print ('You have not enter a name. Please try again!')
                            playerOneName = str(input("Player 1's name:"))
                        else:
                            break
                    playerOne.append(playerOneName)
                    print (playerOneName, "build your team!")
                    print ("1 unit\n2 units\n3 units\n4 units\n5 units")
                    playerOneNumberOfUnits = int(input("How many units in your team?:"))
                    while True:
                        try:
                            if 1<=playerOneNumberOfUnits<=5:
                                break
                            else:
                                print ('Must select between 1 and 5')
                                playerOneNumberOfUnits = int(input("How many units in your team?:"))
                                continue
                            
                        except:
                            continue
                            
            
                        
                        
                    playerOneCharacters (playerOneNumberOfUnits)            
                    print (playerOneName+"\'s"," Team:")
                    print (list(playerOneListOfUnits))
                    #AI
                    print ("VS")
                    # def generateRandomPlayers(playerOneNumberOfUnits):
                    print ("AI TEAM")
                    configOneUnits(playerOneListOfUnits)

                    #AI
                    print ("VS AI TEAM")
                    generateRandomPlayers(playerOneNumberOfUnits)
                    configAIUnits(AIclass)

                elif gameMode == 2: #Player1 vs Player2
                    #PLAYER 1
                    playerOneName = str(input("Player 1's name:"))
                    while True:
                        if playerOneName == '':
                            print ('You have not enter a name. Please try again!')
                            playerOneName = str(input("Player 1's name:"))
                        else:
                            break
                    playerOne.append(playerOneName)
                    print (playerOneName, "build your team!")
                    print ("1 unit\n2 units\n3 units\n4 units\n5 units")
                    playerOneNumberOfUnits = int(input("How many units in your team?:"))
                    while True:
                        try:
                            if 1<=playerOneNumberOfUnits<=5:
                                break
                            else:
                                print ('Must select between 1 and 5')
                                playerOneNumberOfUnits = int(input("How many units in your team?:"))
                                continue
                            
                        except:
                            continue
                    playerOneCharacters (playerOneNumberOfUnits)
                    print (playerOneName+"\'s"," Team:")
                    print (list(playerOneListOfUnits))
                    configOneUnits(playerOneListOfUnits)

                    #PLAYER 2
                    playerTwoName = str(input("Player 2's name:"))
                    while True:
                        if playerTwoName == '':
                            print ('You have not enter a name. Please try again!')
                            playerTwoName = str(input("Player 2's name:"))
                        else:
                            break
                    playerTwo.append(playerTwoName)
                    print (playerTwoName, "build your team!")
                    print ("1 unit\n2 units\n3 units\n4 units\n5 units")
                    playerTwoNumberOfUnits = int(input("How many units in your team?:"))
                    while True:
                        try:
                            if 1<=playerTwoNumberOfUnits<=5:
                                break
                            else:
                                print ('Must select between 1 and 5')
                                playerTwoNumberOfUnits = int(input("How many units in your team?:"))
                                continue
                        except:
                            continue
                    playerTwoCharacters (playerTwoNumberOfUnits)
                    print (playerTwoName +"\'s"," Team:")
                    print (list(playerTwoListOfUnits))
                    configTwoUnits(playerTwoListOfUnits)

                else:
                    print ('Please choose the following game mode')
                    gameMode = int(input("Game mode chosen:"))
                    continue
            except:
                continue
    elif chosenMenu.lower() == 'h':
            f = open("how_to_play.txt", "r")
            print(f.read())
            f.close()
            print (Menu)
            
    elif chosenMenu.lower() == 'e':
        confirmation=input("Are your sure?(Y/N):")
        if confirmation.lower() == 'y':
            print ("Exit Game")
            exit()
        else:
            print ("Invalid Input. Please try again")
            print (Menu)
            continue
    else:
        print ("Invalid Input. Please try again")
        print (Menu)