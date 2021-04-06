import random

VICTORY = "Victoire !"
NULLMATCH = "Ex Aequo ! Encore une manche !"
LOOSE = "Perdu !"
ROCK = "PIERRE"
PAPER = "FEUILLE"
CISOR = "CISEAUX"

def validateMove(move):
    #Take a string and convert it to a move Cisor / Paper / Rock
    if((move == "CISEAUX") or (move =="C")):
        return 2
    elif((move == "PIERRE") or (move == "P")):
        return 0
    elif((move == "FEUILLE") or (move == "F")):
        return 1
    return -1
def checkIfWin(player, bot):
    #Pierre 0 /// Feuille 1 /// Ciseaux 2
    if((player==0 and bot == 1)or(player==1 and bot==2)or(player==2 and bot==0)):
        print(LOOSE)
        return LOOSE
    elif(player==bot):
        print(NULLMATCH)
        return NULLMATCH
    print(VICTORY)
    return VICTORY
    
def randomChoice():    
    return random.randint(0,2)

def getNameOfMove(number):
    if(number == 0):
        return ROCK.lower().capitalize()
    elif(number == 1):
        return PAPER.lower().capitalize()
    elif(number == 2):
        return CISOR.lower().capitalize()


def main():

    #init
    score = 0
    scoreIA = 0
    move_correct = False
    move_player = -1
    still_playing = True
    print("Bienvenue dans le jeu du Chi Fu Mi")

    #Gaming loop
    while still_playing:
        #Loop to wait for a good answer
        while (move_correct != True):
            move = input("Choisissez un mouvement : Ciseaux, Pierre ou Feuille (C/P/F pour faire plus court)").upper()
            move_player = validateMove(move)
            if(move_player>=0):
                move_correct = True
                print("Vous avez choisis : ", getNameOfMove(move_player))
                
        IAChoice = randomChoice()
        print("Votre adversaire artificiel a choisi : ", getNameOfMove(IAChoice))
        result = checkIfWin(move_player, IAChoice)
        #Check if not null
        if result != NULLMATCH:
            still_playing = False
            if result == VICTORY:
                    score += 1
            if result == LOOSE:
                    scoreIA += 1
            print("Votre score est de :", score, "a", scoreIA)
            #Ask for another game
            another_game = input("Encore une partie ? Y/N").upper()
            if another_game == "Y":
                still_playing = True
            else:
                print("Merci d'avoir fait une partie !")
        
        move_correct = False
        


main()
