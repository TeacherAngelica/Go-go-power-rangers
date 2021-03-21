import shutil
import utils
import team
import os
import json
import random

gameFile = open("game.json", "r")
gameJson = gameFile.read()
gameFile.close()
game = json.loads(gameJson)
playerOneName = game['player_one']['name']
playerOneTeam = game['player_one']['team']
playerTwoName = game['player_two']['name']
playerTwoTeam = game['player_two']['team']
playerOne = []
playerTwo = []

def loadGame():
    gameFile = open("game.json", "r")
    gameJson = gameFile.read()
    gameFile.close()
    game = json.loads(gameJson)
    playerOneName = game['player_one']['name']
    playerOneTeam = game['player_one']['team']
    playerTwoName = game['player_two']['name']
    playerTwoTeam = game['player_two']['team']

def playerOneTurn():
    chosenCharacter = input("\n" + playerOneName + ', choose a character: ')
    for character in playerOneTeam:
        if character['name'] == chosenCharacter:
            if character['class'] == 'mage':
                characterAction = input("Order " + character['name'] + ' to [A]ttack or [H]eal?: ')
                targetCharacter = input('Who is your target?: ')
                if characterAction.lower() == 'a':
                    attack('player_two', targetCharacter, 'player_one', chosenCharacter)
                elif characterAction.lower() == 'h':
                    heal('player_one', targetCharacter, chosenCharacter)
            else:
                targetCharacter = input('Who is your target?: ')
                attack('player_two', targetCharacter, 'player_one', chosenCharacter)
    input('Press ENTER to continue...')

def playerTwoTurn():
    chosenCharacter = input("\n" + playerTwoName + ', choose a character: ')
    for character in playerTwoTeam:
        if character['name'] == chosenCharacter:
            if character['class'] == 'mage':
                characterAction = input("Order " + character['name'] + ' to [A]ttack or [H]eal?: ')
                targetCharacter = input('Who is your target?: ')
                if characterAction.lower() == 'a':
                    attack('player_one', targetCharacter, 'player_two', chosenCharacter)
                elif characterAction.lower() == 'h':
                    heal('player_two', targetCharacter, chosenCharacter)
            else:
                targetCharacter = input('Who is your target?: ')
                attack('player_one', targetCharacter, 'player_two', chosenCharacter)
    input('Press ENTER to continue...')

def displayGameStatus():
    utils.clearScreen()
    print(playerOneName + '\'s Team')
    for character in playerOneTeam:
        if character['status'] == 'alive':
            print(character['name'] + ' - ' + 'Health: ' + str(character['attributes']['health']))
    print('\n' + playerTwoName + '\'s Team')
    for character in playerTwoTeam:
        if character['status'] == 'alive':
            print(character['name'] + ' - ' + 'Health: ' + str(character['attributes']['health']))

def attack(targetPlayer, targetCharacter, attackingPlayer, attackingCharacter):
    attackingCharacterAttack = 0
    bonusDamage = random.randint(0, 7)
    hitChance = 1
    for character in game[attackingPlayer]['team']:
        if character['name'] == attackingCharacter:
            if character['class'] == 'troll':
                hitChance = random.randint(0, 1)
            attackingCharacterAttack = character['attributes']['attack']
    characterIndex = 0
    for character in game[targetPlayer]['team']:
        if character['name'] == targetCharacter:
            targetCharacterDefense = character['attributes']['defense']
            totalDamage = 0
            if hitChance == 1:
                totalDamage = attackingCharacterAttack - targetCharacterDefense + bonusDamage
                if totalDamage <= 0:
                    totalDamage = 0
                character['attributes']['health'] = character['attributes']['health'] - totalDamage
            else:
                character['attributes']['health'] = character['attributes']['health'] - totalDamage
            if character['attributes']['health'] <= 0:
                character['status'] = 'fainted'
            updatedGameFile = open("game.json", "r")
            updatedGameJson = updatedGameFile.read()
            updatedGame = json.loads(updatedGameJson)
            updatedGame[targetPlayer]['team'][characterIndex] = character
            with open('game.json', 'w') as outfile:
                json.dump(updatedGame, outfile)
            print("\n" + attackingCharacter + " attacked " + targetCharacter + " and dealt " + str(totalDamage) + " damage!\n")
            characterIndex += 1

def heal(targetPlayer, targetCharacter, healingCharacter):
    characterIndex = 0
    for character in game[targetPlayer]['team']:
        if character['name'] == targetCharacter:
            character['attributes']['health'] = character['attributes']['health'] + 5
            updatedGameFile = open("game.json", "r")
            updatedGameJson = updatedGameFile.read()
            updatedGame = json.loads(updatedGameJson)
            updatedGame[targetPlayer]['team'][characterIndex] = character
            with open('game.json', 'w') as outfile:
                json.dump(updatedGame, outfile)
            print("\n" + healingCharacter + " healed " + targetCharacter + " and restored 5 health!\n")
            characterIndex += 1

def checkWinner():
    gameWinner = None
    isPlayerOneWipedOut = True
    print(gameWinner)
    isPlayerTwoWipedOut = True
    for character in playerOneTeam:
        if character['status'] == 'alive':
            isPlayerOneWipedOut = False
    for character in playerTwoTeam:
        if character['status'] == 'alive':
            isPlayerTwoWipedOut = False
    if isPlayerOneWipedOut == True:
        gameWinner = 'player_two'
    elif isPlayerTwoWipedOut == True:
        gameWinner = 'player_one'
    return gameWinner

def battleStart():
    gameWinner = None
    loadGame()
    while gameWinner == None:
        loadGame()
        displayGameStatus()
        playerOneTurn()

        loadGame()
        gameWinner = checkWinner()
        if gameWinner != None:
            break

        loadGame()
        displayGameStatus()
        playerTwoTurn()

        loadGame()
        gameWinner = checkWinner()
        if gameWinner != None:
            break
    utils.clearScreen()
    winner = None
    if gameWinner == 'player_one':
        winner = playerOneName
    elif gameWinner == 'player_two':
        winner = playerTwoName
    input(winner + " wins the game! Press any key to continue...")
    utils.clearScreen()
    print("Welcome to PSB Battle Game!")
    print("\n[N]ew game \n[R]esume game \n[H]ow to play \n[E]xit\n")

# Game Menu

utils.clearScreen()
print("Welcome to PSB Battle Game!")
print("\n[N]ew game \n[R]esume game \n[H]ow to play \n[E]xit\n")

while True:
    chosenMenu = str(input("Choose an option: "))
    # New Game
    if chosenMenu.lower() == 'n':
        if os.path.exists("game.json"):
            os.remove("game.json")
        shutil.copyfile('init/player_vs_player.json', 'game.json')
        # Player One
        utils.clearScreen()
        playerOneName = str(input("Hello stranger, what is your name?: "))
        playerOne.append(playerOneName)
        utils.clearScreen()
        print("Nice to meet you " + playerOneName + ", let's build your team!\n")
        playerOneNumberOfUnits = int(input("How many characters do you want in your team? (You can select up to five characters): "))
        playerOneTeamComposition = team.build(playerOneNumberOfUnits, 1, playerOneName)
        team.save(playerOneTeamComposition, 1, playerOneName)
        utils.clearScreen()
        # Player Two
        utils.clearScreen()
        playerTwoName = str(input("Hey there other stranger, what is your name?: "))
        playerTwo.append(playerTwoName)
        utils.clearScreen()
        print("Nice to meet you " + playerTwoName + ", let's build your team!\n")
        playerTwoNumberOfUnits = int(input("How many characters do you want in your team? (You can select up to five characters): "))
        playerTwoTeamComposition = team.build(playerTwoNumberOfUnits, 2, playerTwoName)
        team.save(playerTwoTeamComposition, 2, playerTwoName)
        utils.clearScreen()
        loadGame()
        battleStart()
    if chosenMenu.lower() == 'r':
        utils.clearScreen()
        battleStart()
    elif chosenMenu.lower() == 'h':
        utils.clearScreen()
        f = open("how_to_play.txt", "r")
        print(f.read())
        f.close()
        input("\nPress any key to continue...")
        utils.clearScreen()
        print("Welcome to PSB Battle Game!")
        print("\n[N]ew game \n[R]esume game \n[H]ow to play \n[E]xit\n")
    elif chosenMenu.lower() == 'e':
        utils.clearScreen()
        confirmation=input("Are your sure? (y/N): ")
        if confirmation.lower() == 'y':
            exit()
        else:
            utils.clearScreen()
            print("Welcome to PSB Battle Game!")
            print("\n[N]ew game \n[R]esume game \n[H]ow to play \n[E]xit\n")
            continue
    else:
        utils.clearScreen()
        print("Welcome to PSB Battle Game!")
        print("\n[N]ew game \n[R]esume game \n[H]ow to play \n[E]xit\n")