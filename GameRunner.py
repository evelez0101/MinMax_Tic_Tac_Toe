import GameBoard
import random
import MinMax
import time

def main():
    # Create New Board
    board = GameBoard.board()

    # Create a new instance of MinMax
    computer = MinMax.MinMax("O","X")
    test = MinMax.MinMax("X","O")

    # Keeps Track of Turn
    PlayerTurn = True

    # Keep Track of Winner
    PlayerWin = False
    ComputerWin = False
    tie = False

    # Displays the Boardn
    print(board)
        
    # Game Loop
    while(not PlayerWin and not ComputerWin and not tie):
        
        # Check for Tie
        if board.checkTie():
            tie = True

        # Player Turn
        if PlayerTurn and not tie:

           
            # Player Input

            # Always invalid
            playerMove = (-1,-1)
            
            # Checks valid move
            while not board.validateMove(playerMove, "X"): 
                reply = int(input("Input your move (1-9): "))
                playerMove = translate_player_move(reply)
        
            
            # Perfect Strategy Head to head
            #playerMove = test.getMove(board)
        
            board.placePiece(playerMove, "X") 
            PlayerWin = board.checkWin("X")
        
        # Computer Turn
        if not PlayerTurn and not tie:
            
            """
            # Easy Mode
            computerMove = random.choice(board.getAvailableSpots())
            """
            
            # Hard Mode
            computerMove = computer.getMove(board)
        
            board.placePiece(computerMove,"O")
            ComputerWin = board.checkWin("O")
            

        # Slows down the program so we can observe the choice
        time.sleep(0.25)

        # Displays Board
        print(board)
       
        # Switch Turns
        PlayerTurn = not PlayerTurn

    if PlayerWin:
        print("Player Wins!")
    
    if ComputerWin:
        print("Computer Wins!")

    if tie:
        print("Its a tie!")

def translate_player_move(choice):

    choice_to_corrdinate = {1:(0,0), 2:(0,1), 3:(0,2), 
                            4:(1,0), 5:(1,1), 6:(1,2),
                            7:(2,0), 8:(2,1), 9:(2,2)}
    
    # Checks to see if a valid choice is made
    if choice in choice_to_corrdinate:
        return choice_to_corrdinate[choice]

    # Returns on invalid choice
    return (-1,-1)

if __name__ == "__main__":
    main()