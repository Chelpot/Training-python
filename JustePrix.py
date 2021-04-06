import random

def main():
    print("Voici le jeu du juste prix, il te faut deviner un nombre séléctionné aleatoirement entre 0 et 100 inclus")
    playing = True
    while (playing):
        answer = random.randint(0, 100)
        proposition = int(input("Entrez une valeur\n"))
        correct = False
        while (correct==False):
            if(proposition == answer):
                print("Bravo vous avez deviné le prix :", answer)
                correct = True
                playingAgain = input("Voulez vous encore jouer ? Y/N \n")
                if(playingAgain == "N"):
                    playing = False
                    print("Merci d'avoir joué avec nous !")
            elif(proposition > answer):
                proposition = int(input("C'est moins !"))
            elif(proposition < answer):
                proposition = int(input("C'est plus !"))
        
main()
