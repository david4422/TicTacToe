from . import board
from . import player

def playing():   
    game = True
    while game:
        choice = input("Hello my friend, do you want to play a game of tic tac toe? (y/n)")
        if choice == "n":
            break
        b = board.Board()
        pl1 = player.Player("X", b)
        pl2 = player.Player("O", b)

        game_on = True

        while game_on:
            game_over = pl1.make_move()
            if game_over:
                game_on = False
                break
            game_over = pl2.AI_move()
            if game_over:
                game_on = False
                break

        print("good game!!")


        print("do you want to play again? (y/n)")
        if input() == "n":
            game = False
