import random

def get_winner(player_choice, pc_choice):
    if player_choice == pc_choice:
        return "DRAW"
    if player == "rock":
        if pc == "scissors":
            return "PLAYER"
        else:
            return "PC"
    elif player == "paper":
        if pc == "rock":
            return "PLAYER"
        else:
            return "PC"
    elif player == "scissors":
        if pc == "paper":
            return "PLAYER"
        else:
            return "PC"


print("if you are ready to play, write yes or the game going to end...")
ready = input("are you ready to play ropasc?: ")
if ready != "yes":
    print("the game is over, bye...")
else:
    player_skor = 0
    pc_skor = 0
    still_playing = True
    while still_playing:
        options = ["rock", "paper", "scissors"]
        player = input("rock, paper or scissors?: ")
        if player not in options:
            print("rock paper or scissors not a different thing!")
            player = input("rock, paper or scissors?: ")
        else:
            pc = options[random.randint(0, 2)]
            print("pc move: ({}), player move: ({})".format(pc, player))
            winner = get_winner(player_choice=player, pc_choice=pc)
            if winner == "PLAYER":
                player_skor +=1
                print("PLAYER WINS ONE POINT!")
            if winner == "PC":
                pc_skor +=1
                print("PC WINS ONE POINT!")
            if winner == "DRAW":
                print("NO WINNER, DRAW!")
            print("pc score: {}, player score: {}".format(pc_skor, player_skor))

            if player_skor > 2 or pc_skor > 2:
                print("THE GAME IS OVER!")
                still_playing = False
                if player_skor > pc_skor:
                    print("PLAYER WINS THE GAME!")
                else:
                    print("PC WINS THE GAME!")
